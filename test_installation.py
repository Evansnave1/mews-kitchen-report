#!/usr/bin/env python3
"""
Installation Test Script
Verifies that all dependencies are installed correctly
"""

import sys

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing Python dependencies...\n")

    tests = []

    # Test Python version
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        tests.append(False)
    else:
        print("✅ Python version OK\n")
        tests.append(True)

    # Test requests
    try:
        import requests
        print(f"✅ requests installed (version {requests.__version__})")
        tests.append(True)
    except ImportError:
        print("❌ requests not installed - run: pip install requests")
        tests.append(False)

    # Test openpyxl
    try:
        import openpyxl
        print(f"✅ openpyxl installed (version {openpyxl.__version__})")
        tests.append(True)
    except ImportError:
        print("❌ openpyxl not installed - run: pip install openpyxl")
        tests.append(False)

    # Test reportlab
    try:
        import reportlab
        print(f"✅ reportlab installed (version {reportlab.Version})")
        tests.append(True)
    except ImportError:
        print("❌ reportlab not installed - run: pip install reportlab")
        tests.append(False)

    print()

    # Test project modules
    try:
        from mews_client import MewsAPIClient
        print("✅ mews_client.py loaded")
        tests.append(True)
    except ImportError as e:
        print(f"❌ Error loading mews_client.py: {e}")
        tests.append(False)

    try:
        from meal_planner import MealPlanner
        print("✅ meal_planner.py loaded")
        tests.append(True)
    except ImportError as e:
        print(f"❌ Error loading meal_planner.py: {e}")
        tests.append(False)

    try:
        from report_generator import ReportGenerator
        print("✅ report_generator.py loaded")
        tests.append(True)
    except ImportError as e:
        print(f"❌ Error loading report_generator.py: {e}")
        tests.append(False)

    return all(tests)

def test_config():
    """Test configuration file"""
    print("\n" + "="*50)
    print("Testing configuration...\n")

    try:
        import config
        print("✅ config.py found")

        # Check required attributes
        required = ['CLIENT_TOKEN', 'ACCESS_TOKEN', 'BASE_URL']
        missing = []

        for attr in required:
            if not hasattr(config, attr):
                missing.append(attr)

        if missing:
            print(f"⚠️  Missing configuration: {', '.join(missing)}")
            print("   Edit config.py and add these values")
            return False
        else:
            print("✅ All required config values present")

            # Check if using example values
            if config.CLIENT_TOKEN == "your-client-token-here":
                print("⚠️  CLIENT_TOKEN is still the example value")
                print("   Update config.py with your real credentials")
                return False

            print(f"   BASE_URL: {config.BASE_URL}")
            return True

    except ImportError:
        print("❌ config.py not found")
        print("   Run: cp config.example.py config.py")
        print("   Then edit config.py with your credentials")
        return False

def test_files():
    """Test that required files exist"""
    print("\n" + "="*50)
    print("Testing project files...\n")

    from pathlib import Path

    required_files = [
        'mews_client.py',
        'meal_planner.py',
        'report_generator.py',
        'main.py',
        'requirements.txt',
        'README.md',
        'notes.example.json'
    ]

    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} not found")
            all_exist = False

    return all_exist

def main():
    print("="*50)
    print("Kitchen Meal Planner - Installation Test")
    print("="*50)
    print()

    # Run tests
    imports_ok = test_imports()
    files_ok = test_files()
    config_ok = test_config()

    # Summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)

    if imports_ok and files_ok:
        print("✅ All dependencies installed correctly")

        if config_ok:
            print("✅ Configuration file ready")
            print("\n🎉 You're ready to use the application!")
            print("\nNext steps:")
            print("  python main.py --help")
            print("  python main.py --start-date 2024-01-15")
        else:
            print("⚠️  Configuration needs attention")
            print("\nNext steps:")
            print("  1. Update config.py with your Mews credentials")
            print("  2. See GETTING_STARTED.md for details")
    else:
        print("❌ Some issues need to be resolved")
        print("\nNext steps:")
        if not imports_ok:
            print("  1. Install missing dependencies: pip install -r requirements.txt")
        if not files_ok:
            print("  2. Ensure all project files are present")
        if not config_ok:
            print("  3. Create and configure config.py")
        print("  4. Run this test again: python test_installation.py")

    print()

if __name__ == '__main__':
    main()
