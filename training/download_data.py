"""
HeartCheck DL - Kaggle Dataset Downloader
Downloads heart disease datasets from Kaggle using the Kaggle API
"""

import argparse
import os
import zipfile
from pathlib import Path
import subprocess

def download_kaggle_dataset(dataset_slug, output_dir):
    """
    Download dataset from Kaggle using kaggle CLI
    
    Args:
        dataset_slug: Kaggle dataset identifier (e.g., 'fedesoriano/heart-failure-prediction')
        output_dir: Output directory path
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading dataset: {dataset_slug}")
    print(f"Output directory: {output_path.absolute()}")
    
    # Check for Kaggle credentials
    kaggle_json = Path.home() / '.kaggle' / 'kaggle.json'
    if not kaggle_json.exists() and not (os.environ.get('KAGGLE_USERNAME') and os.environ.get('KAGGLE_KEY')):
        print("\n" + "="*60)
        print("ERROR: Kaggle credentials not found!")
        print("="*60)
        print("\nPlease set up Kaggle API credentials:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Click 'Create New API Token'")
        print("3. Save kaggle.json to ~/.kaggle/kaggle.json")
        print("   OR set KAGGLE_USERNAME and KAGGLE_KEY environment variables")
        print("\nFor more info: https://github.com/Kaggle/kaggle-api")
        return False
    
    try:
        # Download using kaggle CLI
        cmd = f'kaggle datasets download -d {dataset_slug} -p {output_path} --unzip'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n✓ Dataset downloaded successfully!")
            print(f"Files saved to: {output_path.absolute()}")
            
            # List downloaded files
            print("\nDownloaded files:")
            for file in output_path.glob('*'):
                if file.is_file():
                    print(f"  - {file.name} ({file.stat().st_size / 1024:.2f} KB)")
            return True
        else:
            print(f"\nERROR downloading dataset:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Download heart disease dataset from Kaggle')
    parser.add_argument('--dataset', '-d', 
                       default='fedesoriano/heart-failure-prediction',
                       help='Kaggle dataset slug (default: fedesoriano/heart-failure-prediction)')
    parser.add_argument('--out', '-o',
                       default='data/raw',
                       help='Output directory (default: data/raw)')
    
    args = parser.parse_args()
    
    print("="*60)
    print("HeartCheck DL - Kaggle Dataset Downloader")
    print("="*60)
    
    success = download_kaggle_dataset(args.dataset, args.out)
    
    if success:
        print("\n✓ Download complete!")
        print("\nNext steps:")
        print("1. Run: python training/prepare_data.py")
        print("2. Run: python training/train_dl.py")
    else:
        print("\n✗ Download failed. Please check the error messages above.")

if __name__ == '__main__':
    main()
