#!/usr/bin/env python3

from scripts.process_templates import TemplateProcessor
from pathlib import Path
import yaml

def debug_template():
    # Test with core config
    with open('examples/core-project-config.yaml') as f:
        config = yaml.safe_load(f)

    print('development_guide in config:', 'development_guide' in config)

    processor = TemplateProcessor(Path('.'))

    try:
        # Try to process development-guide-template
        result = processor.process_template('development-guide-template', config)
        print('Success! Result length:', len(result) if result else 0)
        if result is None:
            print('Result is None')
        elif result == '':
            print('Result is empty string')
        else:
            print('First 200 chars:', repr(result[:200]))
    except Exception as e:
        print('Exception:', e)
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    debug_template()

