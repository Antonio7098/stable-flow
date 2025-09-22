#!/usr/bin/env python3
"""
Stable Flow Template Processing Engine

This script processes Jinja2 templates based on project configuration
to generate customized documentation for different project tiers.
"""

import os
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class TemplateProcessor:
    """Main template processing class"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.templates_dir = project_root / "templates"
        self.source_dir = self.templates_dir / "source"
        self.config_dir = self.templates_dir / "config"
        self.output_dir = project_root / "docs"
        
        # Initialize Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.source_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Add custom filters
        self.jinja_env.filters['strftime'] = self._strftime_filter
    
    def _strftime_filter(self, value: str, format_str: str) -> str:
        """Custom filter for date formatting"""
        if value == "now":
            return datetime.now().strftime(format_str)
        return value
    
    def load_config(self, config_path: Path) -> Dict[str, Any]:
        """Load and validate project configuration"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            # Validate required fields
            self._validate_config(config)
            return config
            
        except FileNotFoundError:
            console.print(f"[red]Error: Configuration file not found: {config_path}[/red]")
            sys.exit(1)
        except yaml.YAMLError as e:
            console.print(f"[red]Error: Invalid YAML in configuration file: {e}[/red]")
            sys.exit(1)
    
    def _validate_config(self, config: Dict[str, Any]) -> None:
        """Validate configuration against schema"""
        required_fields = ['project', 'tier', 'features', 'sections', 'templates']

        for field in required_fields:
            if field not in config:
                console.print(f"[red]Error: Missing required field '{field}' in configuration[/red]")
                sys.exit(1)

        # Validate project has required subfields
        if 'name' not in config['project'] or 'author' not in config['project'] or 'version' not in config['project']:
            console.print("[red]Error: Missing required project fields (name, author, version)[/red]")
            sys.exit(1)

        # Validate tier
        valid_tiers = ['minimal', 'core', 'advanced', 'custom']
        if config['tier'] not in valid_tiers:
            console.print(f"[red]Error: Invalid tier '{config['tier']}'. Must be one of: {valid_tiers}[/red]")
            sys.exit(1)
    
    def process_template(self, template_name: str, config: Dict[str, Any]) -> Optional[str]:
        """Process a single template"""
        try:
            # Try .md first, then .csv
            try:
                template = self.jinja_env.get_template(f"{template_name}.md")
            except TemplateNotFound:
                template = self.jinja_env.get_template(f"{template_name}.csv")
            
            return template.render(**config)
        except TemplateNotFound:
            console.print(f"[yellow]Warning: Template not found: {template_name}.md or {template_name}.csv[/yellow]")
            return None
        except Exception as e:
            console.print(f"[red]Error processing template {template_name}: {e}[/red]")
            return None
    
    def generate_documents(self, config: Dict[str, Any]) -> None:
        """Generate all documents based on configuration"""
        tier = config['tier']
        output_dir = Path(config.get('output', {}).get('directory', 'docs'))
        
        # Create output directory
        output_dir.mkdir(exist_ok=True)
        
        # Determine which templates to process based on tier
        templates_to_process = self._get_templates_for_tier(tier, config)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Generating documents...", total=len(templates_to_process))
            
            for template_name in templates_to_process:
                progress.update(task, description=f"Processing {template_name}...")
                
                content = self.process_template(template_name, config)
                if content:
                    output_path = output_dir / f"{template_name}.md"
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    console.print(f"[green]Generated: {output_path}[/green]")
                
                progress.advance(task)
    
    def _get_templates_for_tier(self, tier: str, config: Dict[str, Any]) -> list:
        """Get list of templates to process based on tier and configuration"""
        if tier == 'minimal':
            return ['prd-template', 'technical-design-template', 'features-csv-template']
        elif tier == 'core':
            return [
                'prd-template', 'technical-design-template', 'features-csv-template',
                'development-guide-template', 'sprint-planning-template', 'sprint-template'
            ]
        elif tier == 'advanced':
            return [
                'prd-template', 'technical-design-template', 'features-csv-template',
                'development-guide-template', 'sprint-planning-template', 'sprint-template',
                'master-index-template', 'adr-template'
            ]
        elif tier == 'custom':
            # For custom tier, use the templates specified in config
            templates = []
            if config.get('templates', {}).get('core', {}).get('prd', False):
                templates.append('prd-template')
            if config.get('templates', {}).get('core', {}).get('technical_design', False):
                templates.append('technical-design-template')
            # Add more as needed
            return templates
        
        return []

@click.command()
@click.option('--config', '-c', default='project-config.yaml', help='Configuration file path')
@click.option('--output', '-o', default='docs', help='Output directory')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def main(config: str, output: str, verbose: bool):
    """Stable Flow Template Processor"""
    project_root = Path.cwd()
    config_path = project_root / config

    if verbose:
        console.print(f"Project root: {project_root}")
        console.print(f"Config file: {config_path}")
        console.print(f"Output directory: {output}")

    try:
        processor = TemplateProcessor(project_root)
        config_data = processor.load_config(config_path)

        # Override output directory if specified
        if output != 'docs':
            config_data['output'] = {'directory': output}

        console.print(f"[blue]Processing templates for tier: {config_data['tier']}[/blue]")
        processor.generate_documents(config_data)
        console.print("[green]Document generation complete![/green]")
    except SystemExit as e:
        # Validation or processing failed, exit with error code
        sys.exit(e.code if hasattr(e, 'code') else 1)

if __name__ == '__main__':
    main()
