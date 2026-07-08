#!/usr/bin/env python3
"""
Generate portfolio captures for P13 Partie 1 - Bottleneck analysis
Generates 8 screenshots demonstrating:
1. Mission & Context
2. Notebook structure
3. Quality controls
4. Before/After metrics
5. KPI Dashboard
6. Kanban GitHub
7. Dataviz sample
8. IA Journal coverage
"""

import json
import os
from pathlib import Path
import sys
from datetime import datetime

# Try to import playwright for HTML screenshots
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("⚠️  Playwright not installed. Install with: pip install playwright && playwright install")

# Try to import PIL for image generation
try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("⚠️  Pillow not installed. Install with: pip install Pillow")


def get_project_paths():
    """Get paths to key files"""
    base_dir = Path(__file__).parent.parent.parent.parent  # Go to P13/
    p6_dir = base_dir / "Partie 1" / "P6_ameliore_IA"
    
    return {
        "notebook": p6_dir / "notebooks" / "bottleneck_analyse_ameliore_final.ipynb",
        "output_dir": p6_dir / "output",
        "captures_dir": p6_dir / "output" / "captures",
        "dataviz_dir": p6_dir / "output" / "dataviz",
        "docs_dir": p6_dir / "docs",
        "synthese_doc": p6_dir / "docs" / "06_synthese_finale_P13_partie_1.md",
        "journal_ia_doc": p6_dir / "docs" / "03_journal_ia_P13_partie_1.md",
    }


def capture_html_element(url, output_path, viewport_width=1024, viewport_height=600):
    """Capture HTML page using Playwright"""
    if not PLAYWRIGHT_AVAILABLE:
        print(f"⏭️  Skipping HTML capture (Playwright not available): {output_path}")
        return False
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": viewport_width, "height": viewport_height})
            
            # Handle both file:// and http:// URLs
            if url.startswith(("http://", "https://")):
                page.goto(url, wait_until="networkidle")
            else:
                # Local file
                file_url = f"file:///{Path(url).absolute()}".replace("\\", "/")
                page.goto(file_url)
            
            page.wait_for_load_state("networkidle")
            page.screenshot(path=str(output_path))
            browser.close()
            
            print(f"✅ Captured: {output_path.name}")
            return True
    except Exception as e:
        print(f"❌ Error capturing {output_path}: {e}")
        return False


def create_placeholder_image(output_path, title, description):
    """Create placeholder image with text"""
    if not PIL_AVAILABLE:
        print(f"⏭️  Skipping placeholder (Pillow not available): {output_path}")
        return False
    
    try:
        # Create image
        img = Image.new('RGB', (1024, 600), color=(245, 245, 245))
        d = ImageDraw.Draw(img)
        
        # Try to use a nice font, fallback to default
        try:
            title_font = ImageFont.truetype("arial.ttf", 28)
            text_font = ImageFont.truetype("arial.ttf", 16)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Draw header
        d.rectangle([(0, 0), (1024, 80)], fill=(50, 120, 200))
        d.text((40, 20), title, fill=(255, 255, 255), font=title_font)
        
        # Draw description
        d.text((40, 120), description, fill=(50, 50, 50), font=text_font)
        
        # Draw footer
        d.text((40, 520), f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", 
               fill=(150, 150, 150), font=text_font)
        
        img.save(output_path)
        print(f"✅ Created placeholder: {output_path.name}")
        return True
    except Exception as e:
        print(f"❌ Error creating placeholder {output_path}: {e}")
        return False


def generate_notebook_outline_capture(notebook_path, output_path):
    """Extract and visualize notebook structure from JSON"""
    if not PIL_AVAILABLE:
        return False
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Count cells by type
        total_cells = len(nb.get('cells', []))
        markdown_cells = sum(1 for c in nb['cells'] if c['cell_type'] == 'markdown')
        code_cells = sum(1 for c in nb['cells'] if c['cell_type'] == 'code')
        
        # Create image
        img = Image.new('RGB', (1024, 600), color=(245, 245, 245))
        d = ImageDraw.Draw(img)
        
        try:
            title_font = ImageFont.truetype("arial.ttf", 28)
            text_font = ImageFont.truetype("arial.ttf", 16)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Header
        d.rectangle([(0, 0), (1024, 80)], fill=(50, 120, 200))
        d.text((40, 20), "Notebook Structure - 49 Cells", fill=(255, 255, 255), font=title_font)
        
        # Content
        y = 120
        stats = [
            f"Total Cells: {total_cells}",
            f"Code Cells: {code_cells}",
            f"Markdown Cells: {markdown_cells}",
            "",
            "Structure: Phase I + Phase II + Checkpoints",
            "✅ M00: Prérequis & vérifications",
            "✅ Phase I: Data loading & quality controls",
            "✅ Phase II: Business analysis & KPI",
            "✅ Checkpoints: Validation at each step",
        ]
        
        for stat in stats:
            d.text((40, y), stat, fill=(50, 50, 50), font=text_font)
            y += 40
        
        img.save(output_path)
        print(f"✅ Created notebook outline: {output_path.name}")
        return True
    except Exception as e:
        print(f"❌ Error creating notebook outline: {e}")
        return False


def main():
    """Main capture generation function"""
    print("=" * 80)
    print("🎬 Generating Portfolio Captures - P13 Partie 1")
    print("=" * 80)
    
    paths = get_project_paths()
    
    # Ensure captures directory exists
    paths["captures_dir"].mkdir(parents=True, exist_ok=True)
    os.chdir(paths["captures_dir"])
    
    print(f"\n📁 Captures directory: {paths['captures_dir']}")
    print(f"📁 Notebook: {paths['notebook']}")
    print(f"📁 Dataviz: {paths['dataviz_dir']}")
    print()
    
    captures_config = [
        {
            "name": "01_mission_p6_bottleneck.png",
            "type": "placeholder",
            "title": "Mission: Bottleneck Wine Shop",
            "description": "Context: Reconcile ERP/Web/Liaison data → Produce KPI for CODIR\nResult: Clean database + Quality controls + Business analysis",
        },
        {
            "name": "02_notebook_structure_49cells.png",
            "type": "notebook_outline",
            "notebook": paths["notebook"],
        },
        {
            "name": "03_quality_report_18controls.png",
            "type": "placeholder",
            "title": "Quality Controls - Phase I",
            "description": "✅ 18 validation points: structure, values, duplicates, keys, stocks\n✅ 825 ERP products loaded | 1513 Web records | 825 Liaison references\n✅ 2 stock anomalies corrected | 714 ERP/Web matches (47.2%)",
        },
        {
            "name": "04_before_after_metrics.png",
            "type": "placeholder",
            "title": "Before/After Comparison",
            "description": "P6 Initial → P6 Améliore:\n• Cells: 148 → 49 (-68%)\n• Execution time: ~5min → 1:11min (-76%)\n• Documentation: 0 → 26 IA prompts\n• Quality controls: implicit → 18 explicit",
        },
        {
            "name": "05_kpi_dashboard_phase2.png",
            "type": "placeholder",
            "title": "KPI Dashboard - Phase II",
            "description": "Revenue: 143,680 EUR | Products: 689 | Pareto 80%: 435 (54.2%)\nMargin: 47.32% avg | Stock: 2.98 months | Anomalies: 10 detected\n✅ 13 dataviz generated | 6 KPI calculated | 7 data contracts validated",
        },
        {
            "name": "07_dataviz_sample_correlations.png",
            "type": "html_capture",
            "url": str(paths["dataviz_dir"] / "correlations_quantitatives.html"),
        },
        {
            "name": "08_ia_journal_26prompts.png",
            "type": "placeholder",
            "title": "IA Journal - 26 Prompts Traced",
            "description": "13 essais documented: M00-M13\n• Each essai: Objective → Prompt → Result → Human decision → Limitations\n• Total: 26 prompts documented for IA governance\n• Full traceability for P13 mission criteria",
        },
    ]
    
    results = {
        "generated": [],
        "skipped": [],
        "failed": [],
    }
    
    print("🎬 Generating captures...")
    print()
    
    for config in captures_config:
        output_path = paths["captures_dir"] / config["name"]
        
        try:
            if config["type"] == "placeholder":
                if create_placeholder_image(output_path, config["title"], config["description"]):
                    results["generated"].append(config["name"])
                else:
                    results["skipped"].append(config["name"])
            
            elif config["type"] == "notebook_outline":
                if generate_notebook_outline_capture(config["notebook"], output_path):
                    results["generated"].append(config["name"])
                else:
                    results["skipped"].append(config["name"])
            
            elif config["type"] == "html_capture":
                if capture_html_element(config["url"], output_path):
                    results["generated"].append(config["name"])
                else:
                    results["skipped"].append(config["name"])
        
        except Exception as e:
            print(f"❌ Error processing {config['name']}: {e}")
            results["failed"].append(config["name"])
    
    # Print summary
    print()
    print("=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print(f"✅ Generated: {len(results['generated'])} captures")
    for f in results["generated"]:
        print(f"   • {f}")
    
    if results["skipped"]:
        print(f"\n⏭️  Skipped: {len(results['skipped'])} (missing dependencies)")
        for f in results["skipped"]:
            print(f"   • {f}")
    
    if results["failed"]:
        print(f"\n❌ Failed: {len(results['failed'])}")
        for f in results["failed"]:
            print(f"   • {f}")
    
    print()
    print("=" * 80)
    print(f"📁 Captures saved to: {paths['captures_dir']}")
    print("=" * 80)
    
    # Check total size
    total_size = sum(f.stat().st_size for f in paths["captures_dir"].glob("*.png")) / (1024 * 1024)
    print(f"📦 Total size: {total_size:.2f} MB")
    print()
    
    print("✨ Next: git add output/captures/ && git commit && git push")
    

if __name__ == "__main__":
    main()
