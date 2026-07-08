#!/usr/bin/env python3
"""
Verify captures and prepare for git commit
"""

from pathlib import Path
import os

def main():
    captures_dir = Path("Partie 1/P6_ameliore_IA/output/captures")
    
    print("=" * 80)
    print("📸 CAPTURES VERIFICATION & PUBLICATION CHECKLIST")
    print("=" * 80)
    print()
    
    # List all PNG files
    png_files = sorted(captures_dir.glob("*.png"))
    
    print(f"📁 Captures directory: {captures_dir}")
    print(f"📊 Total PNG files: {len(png_files)}")
    print()
    
    if not png_files:
        print("❌ No captures found!")
        return False
    
    # Verify & list each capture
    total_size = 0
    print("✅ Captures found:")
    for i, f in enumerate(png_files, 1):
        size_kb = f.stat().st_size / 1024
        size_mb = f.stat().st_size / (1024 * 1024)
        total_size += f.stat().st_size
        
        print(f"   {i}. {f.name:45} ({size_kb:6.1f} KB)")
    
    total_size_mb = total_size / (1024 * 1024)
    print()
    print(f"📦 Total size: {total_size_mb:.2f} MB")
    print()
    
    # Verify quality
    expected_captures = {
        "01_mission_p6_bottleneck.png": "Mission & Context",
        "03_quality_report_18controls.png": "Quality Controls",
        "04_before_after_metrics.png": "Before/After Metrics",
        "05_kpi_dashboard_phase2.png": "KPI Dashboard",
        "08_ia_journal_26prompts.png": "IA Journal",
    }
    
    print("✅ Quality checklist:")
    for filename, description in expected_captures.items():
        f = captures_dir / filename
        if f.exists():
            print(f"   ✅ {filename:45} ({description})")
        else:
            print(f"   ❌ {filename:45} ({description}) - MISSING")
    
    print()
    print("=" * 80)
    print("🚀 NEXT STEPS FOR PUBLICATION")
    print("=" * 80)
    print()
    print("1. Verify captures look good in output/captures/")
    print()
    print("2. Git commands:")
    print("   git add 'Partie 1/P6_ameliore_IA/output/captures/'")
    print("   git commit -m 'Add portfolio captures (8 images, <1 MB)'")
    print("   git push origin main")
    print()
    print("3. GitHub:")
    print("   - Make repo public")
    print("   - Verify captures visible on GitHub")
    print("   - Update README.md if needed")
    print()
    print("=" * 80)
    print("✨ All set for publication! 🎉")
    print("=" * 80)


if __name__ == "__main__":
    main()
