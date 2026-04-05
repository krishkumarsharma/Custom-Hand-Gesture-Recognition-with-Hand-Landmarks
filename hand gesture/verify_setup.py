#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verification script to check if all necessary modules and files are in place.
"""
import sys
import os

def verify_imports():
    """Verify all required imports work."""
    print("=" * 60)
    print("VERIFYING HAND GESTURE RECOGNITION SETUP")
    print("=" * 60)
    
    errors = []
    
    # Check Python version
    print(f"\n✓ Python version: {sys.version.split()[0]}")
    
    # Check required directories
    print("\nChecking directories...")
    required_dirs = ['model', 'utils', 'model/keypoint_classifier', 'model/point_history_classifier']
    for dir_path in required_dirs:
        if os.path.isdir(dir_path):
            print(f"  ✓ {dir_path}/")
        else:
            print(f"  ✗ {dir_path}/ NOT FOUND")
            errors.append(f"Missing directory: {dir_path}")
    
    # Check required files
    print("\nChecking files...")
    required_files = [
        'app.py',
        'mediapipetest.py',
        'model/__init__.py',
        'model/keypoint_classifier/keypoint_classifier.py',
        'model/keypoint_classifier/keypoint_classifier_label.csv',
        'model/point_history_classifier/point_history_classifier.py',
        'model/point_history_classifier/point_history_classifier_label.csv',
        'utils/__init__.py',
        'utils/cvfpscalc.py'
    ]
    for file_path in required_files:
        if os.path.isfile(file_path):
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} NOT FOUND")
            errors.append(f"Missing file: {file_path}")
    
    # Try importing main dependencies
    print("\nImporting core libraries...")
    imports_to_test = [
        ('cv2', 'OpenCV'),
        ('mediapipe', 'MediaPipe'),
        ('numpy', 'NumPy'),
    ]
    
    for module_name, display_name in imports_to_test:
        try:
            mod = __import__(module_name)
            version = getattr(mod, '__version__', 'unknown')
            print(f"  ✓ {display_name} ({module_name}) - version: {version}")
        except ImportError as e:
            print(f"  ✗ {display_name} ({module_name}) - ERROR: {e}")
            errors.append(f"Failed to import {module_name}: {e}")
    
    # Try importing TensorFlow (with timeout handling)
    print("\nImporting TensorFlow (this may take a moment)...")
    try:
        import tensorflow as tf
        print(f"  ✓ TensorFlow (tensorflow) - version: {tf.__version__}")
    except Exception as e:
        print(f"  ✗ TensorFlow - ERROR: {e}")
        errors.append(f"Failed to import TensorFlow: {e}")
    
    # Try importing local modules
    print("\nImporting local modules...")
    try:
        from utils import CvFpsCalc
        print(f"  ✓ CvFpsCalc (from utils)")
    except ImportError as e:
        print(f"  ✗ CvFpsCalc - ERROR: {e}")
        errors.append(f"Failed to import CvFpsCalc: {e}")
    
    try:
        from model import KeyPointClassifier
        print(f"  ✓ KeyPointClassifier (from model)")
    except Exception as e:
        print(f"  ✗ KeyPointClassifier - ERROR: {e}")
        errors.append(f"Failed to import KeyPointClassifier: {e}")
    
    try:
        from model import PointHistoryClassifier
        print(f"  ✓ PointHistoryClassifier (from model)")
    except Exception as e:
        print(f"  ✗ PointHistoryClassifier - ERROR: {e}")
        errors.append(f"Failed to import PointHistoryClassifier: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    if errors:
        print(f"❌ SETUP VERIFICATION FAILED - {len(errors)} issue(s) found:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        return False
    else:
        print("✅ ALL CHECKS PASSED - Setup is ready!")
        return True

if __name__ == '__main__':
    success = verify_imports()
    sys.exit(0 if success else 1)
