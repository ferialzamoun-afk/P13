# Script optionnel - Vérification de qualité de code Ruff + nbQA
# Objectif : Lancer des vérifications de style Python et notebook
# Usage : .\lint_notebook.ps1

param(
    [string]$NotebookPath = "../notebooks/bottleneck_analyse_ameliore_final.ipynb",
    [string]$OutputFile = "./lint_report.txt",
    [bool]$Verbose = $true
)

Write-Host "=" * 80
Write-Host "🔍 VÉRIFICATION QUALITÉ DE CODE - RUFF + nbQA"
Write-Host "=" * 80

# Vérifie que les outils sont installés
$tools_required = @("ruff", "nbqa")
$tools_missing = @()

foreach ($tool in $tools_required) {
    try {
        $version = & $tool --version 2>&1 | Select-Object -First 1
        if ($Verbose) { Write-Host "✅ $tool: $version" }
    }
    catch {
        Write-Host "❌ $tool: NON INSTALLÉ"
        $tools_missing += $tool
    }
}

if ($tools_missing.Count -gt 0) {
    Write-Host ""
    Write-Host "⚠️  OUTILS MANQUANTS:"
    foreach ($tool in $tools_missing) {
        Write-Host "   Installer avec: pip install $tool"
    }
    exit 1
}

Write-Host ""
Write-Host "-" * 80
Write-Host "📝 LANCEMENT DES VÉRIFICATIONS..."
Write-Host "-" * 80

# Ajouter rapport à fichier
$report_content = @()
$report_content += "RAPPORT DE QUALITÉ CODE - Bottleneck Notebook"
$report_content += "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$report_content += ""

try {
    # 1. Vérification Ruff sur le notebook
    Write-Host ""
    Write-Host "1️⃣  Vérification RUFF (linting Python)..."
    $report_content += "1. RUFF - Linting Python"
    $report_content += "-" * 40
    
    $ruff_output = & nbqa ruff check "$NotebookPath" --select E,F,W 2>&1
    if ($LASTEXITCODE -eq 0) {
        $report_content += "✅ Aucun problème détecté"
        Write-Host "   ✅ Aucun problème détecté"
    }
    else {
        $report_content += $ruff_output | ConvertTo-Json
        Write-Host "   ⚠️  Problèmes détectés (voir rapport)"
    }
    $report_content += ""
}
catch {
    Write-Host "   ⚠️  Ruff introuvable ou erreur d'exécution"
    $report_content += "⚠️  Ruff introuvable"
}

try {
    # 2. Vérification de complexité
    Write-Host ""
    Write-Host "2️⃣  Vérification nbQA..."
    $report_content += "2. nbQA - Analyse notebook"
    $report_content += "-" * 40
    
    $nbqa_output = & nbqa flake8 "$NotebookPath" --select E,W 2>&1
    if ($LASTEXITCODE -eq 0) {
        $report_content += "✅ Aucun problème détecté"
        Write-Host "   ✅ Aucun problème détecté"
    }
    else {
        $report_content += "⚠️  Vérification partielle (pep8)"
        Write-Host "   ⚠️  Vérification partielle"
    }
    $report_content += ""
}
catch {
    Write-Host "   ⚠️  nbQA introuvable"
    $report_content += "⚠️  nbQA introuvable"
}

Write-Host ""
Write-Host "-" * 80
Write-Host "✅ VÉRIFICATIONS TERMINÉES"
Write-Host "-" * 80

# Sauvegarder le rapport
try {
    $report_content | Out-File -FilePath $OutputFile -Encoding UTF8
    Write-Host ""
    Write-Host "📄 Rapport sauvegardé: $OutputFile"
}
catch {
    Write-Host "⚠️  Impossible de sauvegarder le rapport"
}

Write-Host ""
Write-Host "=" * 80
Write-Host "💡 NOTES:"
Write-Host "  - Cet audit est optionnel et complémentaire"
Write-Host "  - L'exécution du notebook reste prioritaire"
Write-Host "  - Les problèmes détectés ne bloquent pas l'analyse"
Write-Host "=" * 80
