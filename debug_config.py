#!/usr/bin/env python3

def minimal_config():
    """Minimal tier configuration for testing"""
    return {
        'project': {
            'name': 'Test Project',
            'description': 'A test project',
            'author': 'Test Author',
            'version': '1.0.0',
            'created': '2024-12-09'
        },
        'tier': 'minimal',
        'features': {
            'cascade': False
        },
        'sections': {
            'prd': {
                'competitive_analysis': False,
                'user_experience': False,
                'data_strategy': False,
                'competitive_moat': False,
                'monetization': False
            },
            'technical_design': {
                'accessibility': False,
                'security_detailed': False,
                'api_specification': False,
                'architectural_decisions': False
            },
            'sprint_template': {
                'parallel_agents': False,
                'environmental_impact': False,
                'api_integration': False
            },
            'sprint_planning': {
                'ai_assisted_velocity': False,
                'ai_specific_risks': False
            },
            'features_csv': {
                'business_metrics': False,
                'sprint_assignment': False,
                'risk_level': False
            }
        },
        'templates': {
            'core': {
                'prd': True,
                'technical_design': True,
                'features_csv': True,
                'development_guide': False,
                'sprint_planning': False,
                'sprint_template': False,
                'master_index': False
            }
        },
        'output': {
            'directory': 'docs',
            'format': 'markdown',
            'include_toc': True,
            'include_metadata': True
        },
        'prd': {
            'version': '1.0',
            'last_updated': '2024-12-09',
            'stakeholders': 'Test Team',
            'vision': 'Test vision',
            'primary_goal': 'Test goal',
            'success_metrics': 'Test metrics',
            'target_users': 'Test users',
            'competitors': [],
            'market_opportunities': [],
            'personas': [],
            'wireframes': {},
            'ab_tests': [],
            'i18n': {},
            'data': {},
            'moat': {},
            'revenue_streams': [],
            'features': [],
            'mvp_features': [],
            'post_mvp_features': [],
            'technical': {
                'performance': {
                    'response_time': '< 2 seconds',
                    'throughput': '100 requests/second',
                    'availability': '99.9%'
                },
                'security': {
                    'authentication': 'Basic auth',
                    'data_protection': 'Encrypted storage',
                    'compliance': 'Basic security standards'
                },
                'integrations': []
            },
            'timeline': {
                'phases': [],
                'milestones': []
            },
            'risks': {
                'technical': [],
                'business': []
            },
            'kpis': {
                'primary': [],
                'secondary': []
            },
            'dependencies': {
                'external': [],
                'internal': []
            },
            'assumptions': [],
            'references': [],
            'glossary': {}
        },
        'technical_design': {
            'version': '1.0',
            'last_updated': '2024-12-09',
            'reviewers': 'Test Reviewers',
            'system_purpose': 'Test system',
            'tech_stack': {
                'frontend': 'React',
                'backend': 'Node.js',
                'database': 'PostgreSQL',
                'infrastructure': 'AWS',
                'devops': 'Docker'
            },
            'architecture_diagram': 'graph TB\n    A[Component A] --> B[Component B]',
            'components': [],
            'data_models': [],
            'database': {
                'primary': 'PostgreSQL',
                'caching': 'Redis',
                'backup': 'Basic backup',
                'migration': 'Manual migration'
            },
            'data_flow_diagram': 'graph LR\n    A[User] --> B[System] --> C[Database]',
            'security': {
                'auth_method': 'Basic auth',
                'authz_model': 'Simple',
                'session_mgmt': 'Sessions',
                'encryption_at_rest': 'Basic encryption',
                'encryption_in_transit': 'HTTPS',
                'key_management': 'Basic',
                'data_classification': 'Basic'
            },
            'api': {
                'version': '1.0.0',
                'base_url': 'https://api.example.com',
                'auth': 'API Key',
                'versioning': {
                    'strategy': 'URL versioning',
                    'deprecation': '6 months notice',
                    'compatibility': 'Backward compatible'
                },
                'endpoints': []
            },
            'performance': {
                'api_response': '< 1s',
                'page_load': '< 2s',
                'db_queries': '< 100ms',
                'concurrent_users': '100',
                'rps': '10',
                'data_processing': 'Real-time',
                'scaling': {
                    'horizontal': 'Load balancer',
                    'vertical': 'Instance upgrade'
                },
                'caching': 'Browser cache'
            },
            'integrations': {
                'external': [],
                'internal': []
            },
            'deployment': {
                'compute': '1 vCPU, 1GB RAM',
                'network': 'Basic networking',
                'storage': '10GB storage',
                'cicd': {
                    'source_control': 'Git',
                    'build': 'Manual build',
                    'testing': 'Manual testing',
                    'deployment': 'Manual deployment'
                },
                'environments': {
                    'development': 'Local development',
                    'staging': 'Basic staging',
                    'production': 'Production server'
                }
            },
            'monitoring': {
                'logging': {
                    'levels': 'INFO, ERROR',
                    'aggregation': 'Basic logging',
                    'retention': '30 days'
                },
                'metrics': {
                    'application': 'Basic metrics',
                    'infrastructure': 'Server metrics',
                    'business': 'Usage metrics'
                },
                'alerting': {
                    'critical': 'System down',
                    'warning': 'High load',
                    'channels': 'Email'
                }
            },
            'ai_prompts': {
                'primary': 'You are a senior software architect helping with technical design and implementation.',
                'context': 'Focus on modern best practices and scalable architecture',
                'version_control': 'Git-based prompt versioning',
                'testing': 'A/B testing of prompts',
                'performance': 'Monitor prompt effectiveness',
                'ethics': {
                    'bias': 'Ensure unbiased technical decisions',
                    'transparency': 'Document AI-assisted decisions',
                    'oversight': 'Human review of critical decisions'
                }
            },
            'references': [],
            'glossary': {}
        }
    }

def core_config(minimal_config):
    """Core tier configuration for testing"""
    config = minimal_config.copy()
    config['tier'] = 'core'
    config['features']['cascade'] = True
    config['sections']['prd']['competitive_analysis'] = True
    config['sections']['prd']['user_experience'] = True
    config['sections']['technical_design']['accessibility'] = True
    config['sections']['technical_design']['security_detailed'] = True
    config['sections']['technical_design']['api_specification'] = True
    config['sections']['technical_design']['architectural_decisions'] = True
    config['sections']['sprint_template']['parallel_agents'] = True
    config['sections']['sprint_template']['api_integration'] = True
    config['sections']['sprint_planning']['ai_assisted_velocity'] = True
    config['sections']['sprint_planning']['ai_specific_risks'] = True
    config['sections']['features_csv']['business_metrics'] = True
    config['sections']['features_csv']['sprint_assignment'] = True
    config['sections']['features_csv']['risk_level'] = True
    config['templates']['core']['development_guide'] = True
    config['templates']['core']['sprint_planning'] = True
    config['templates']['core']['sprint_template'] = True

    # Add core tier data
    config['development_guide'] = {
        'version': '1.0',
        'last_updated': '2024-12-09',
        'coding_standards': {},
        'general_principles': [],
        'code_review_checklist': [],
        'project_structure': '',
        'file_naming': [],
        'import_organization': [],
        'git': {
            'branching_strategy': 'GitFlow with feature branches',
            'commit_convention': 'Conventional Commits',
            'pr_process': []
        },
        'testing': {'levels': {}, 'organization': '', 'mocking': ''},
        'error_handling': {'types': {}, 'logging': [], 'monitoring': ''},
        'performance': {'frontend': [], 'backend': [], 'database': [], 'caching': ''},
        'security': {'auth': [], 'data_protection': [], 'input_validation': [], 'headers': []},
        'modern_paradigms': {'best_practices': [], 'design_patterns': {}, 'architecture': []},
        'automation': {'pre_commit_hooks': [], 'pr_automation': [], 'automated_testing': []},
        'profiling': {'frontend': [], 'backend': [], 'monitoring': []},
        'scripts': {'development': {}, 'build': {}, 'deployment': {}},
        'anti_patterns': {'code_quality': [], 'security': [], 'performance': [], 'architecture': []},
        'references': [],
        'glossary': {},
        'tools': {}
    }

    return config

if __name__ == '__main__':
    min_cfg = minimal_config()
    core_cfg = core_config(min_cfg)
    print('development_guide in core_config:', 'development_guide' in core_cfg)
    print('Keys in core_config:', sorted(core_cfg.keys()))

