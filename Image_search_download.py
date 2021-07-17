#!/usr/bin/env python3
from bing_image_downloader import downloader
downloader.download('Mbappé', limit=1000,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=30)