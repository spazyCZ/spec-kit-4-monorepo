#!/usr/bin/env python3
"""
Validate Spec-Driven Development workflow artifacts.

This script checks that all required files exist for a feature specification
and validates they follow the expected structure.
"""

import sys
from pathlib import Path
from typing import List, Tuple


def validate_feature_structure(feature_dir: Path) -> List[Tuple[str, bool, str]]:
    """
    Validate that a feature directory has the expected structure.
    
    Returns list of (check_name, passed, message) tuples.
    """
    checks = []
    
    # Check required files
    spec_file = feature_dir / "spec.md"
    checks.append((
        "Specification exists",
        spec_file.exists(),
        f"spec.md {'found' if spec_file.exists() else 'missing'}"
    ))
    
    plan_file = feature_dir / "plan.md"
    checks.append((
        "Implementation plan exists",
        plan_file.exists(),
        f"plan.md {'found' if plan_file.exists() else 'missing'}"
    ))
    
    research_file = feature_dir / "research.md"
    checks.append((
        "Research document exists",
        research_file.exists(),
        f"research.md {'found' if research_file.exists() else 'missing (optional)'}"
    ))
    
    data_model_file = feature_dir / "data-model.md"
    checks.append((
        "Data model exists",
        data_model_file.exists(),
        f"data-model.md {'found' if data_model_file.exists() else 'missing (optional)'}"
    ))
    
    contracts_dir = feature_dir / "contracts"
    checks.append((
        "Contracts directory exists",
        contracts_dir.exists(),
        f"contracts/ {'found' if contracts_dir.exists() else 'missing (optional)'}"
    ))
    
    tasks_file = feature_dir / "tasks.md"
    checks.append((
        "Tasks breakdown exists",
        tasks_file.exists(),
        f"tasks.md {'found' if tasks_file.exists() else 'missing (run /speckit.tasks)'}"
    ))
    
    # Check constitution
    constitution_file = feature_dir.parent.parent / "memory" / "constitution.md"
    checks.append((
        "Constitution exists",
        constitution_file.exists(),
        f"constitution.md {'found' if constitution_file.exists() else 'missing (run /speckit.constitution)'}"
    ))
    
    return checks


def validate_spec_content(spec_file: Path) -> List[Tuple[str, bool, str]]:
    """
    Validate specification file content.
    
    Returns list of (check_name, passed, message) tuples.
    """
    checks = []
    
    if not spec_file.exists():
        return [("Spec file readable", False, "File does not exist")]
    
    content = spec_file.read_text()
    
    # Check for user stories
    has_user_stories = "### User Story" in content or "## User Scenarios" in content
    checks.append((
        "Contains user stories",
        has_user_stories,
        "User stories section found" if has_user_stories else "Missing user stories"
    ))
    
    # Check for requirements
    has_requirements = "### Functional Requirements" in content
    checks.append((
        "Contains functional requirements",
        has_requirements,
        "Functional requirements found" if has_requirements else "Missing functional requirements"
    ))
    
    # Check for acceptance scenarios
    has_acceptance = "**Given**" in content and "**When**" in content and "**Then**" in content
    checks.append((
        "Contains acceptance scenarios",
        has_acceptance,
        "Acceptance scenarios found" if has_acceptance else "Missing Given-When-Then scenarios"
    ))
    
    # Check for excessive clarification markers
    clarification_count = content.count("[NEEDS CLARIFICATION")
    checks.append((
        "Limited clarification markers",
        clarification_count <= 3,
        f"{clarification_count} clarification markers (max recommended: 3)"
    ))
    
    # Check for priorities
    has_priorities = "Priority: P1" in content or "Priority: P2" in content
    checks.append((
        "User stories prioritized",
        has_priorities,
        "Priorities found" if has_priorities else "Missing priority markers (P1, P2, P3)"
    ))
    
    return checks


def print_results(checks: List[Tuple[str, bool, str]], title: str):
    """Print validation results."""
    print(f"\n{title}")
    print("=" * 60)
    
    passed = sum(1 for _, p, _ in checks if p)
    total = len(checks)
    
    for name, passed_check, message in checks:
        status = "✓" if passed_check else "✗"
        print(f"{status} {name}: {message}")
    
    print(f"\nPassed: {passed}/{total}")


def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: validate_workflow.py <feature-directory>")
        print("\nExample:")
        print("  validate_workflow.py specs/001-todo-api")
        sys.exit(1)
    
    feature_path = Path(sys.argv[1])
    
    if not feature_path.exists():
        print(f"Error: Directory not found: {feature_path}")
        sys.exit(1)
    
    if not feature_path.is_dir():
        print(f"Error: Not a directory: {feature_path}")
        sys.exit(1)
    
    print(f"Validating feature: {feature_path}")
    
    # Validate structure
    structure_checks = validate_feature_structure(feature_path)
    print_results(structure_checks, "Structure Validation")
    
    # Validate spec content
    spec_file = feature_path / "spec.md"
    if spec_file.exists():
        content_checks = validate_spec_content(spec_file)
        print_results(content_checks, "Specification Content Validation")
    
    # Overall summary
    all_checks = structure_checks + (content_checks if spec_file.exists() else [])
    all_passed = all(passed for _, passed, _ in all_checks)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All validations passed!")
        sys.exit(0)
    else:
        print("✗ Some validations failed. Review the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
