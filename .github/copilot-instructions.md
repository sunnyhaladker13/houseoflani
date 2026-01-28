# House of Lani - Copilot Instructions

## Project Overview

House of Lani is a wellness sanctuary website focused on intentional living, movement, and recovery. The design aesthetic is "Luxury," "Calm," and "Refined."

## Visual Language & Design System

When generating code or content, adhere to these visual principles:

### 1. Typography

- **Headings**: Use `var(--font-heading)` ('IvyOra Display' / 'Playfair Display'). Tone should be elegant and welcoming.
- **Body**: Use `var(--font-body)` ('General Sans'). Keep weight light (`300`) and line-height generous (`1.8`) for readability.

### 2. Color Palette

Always use the defined CSS variables found in `assets/css/styles.css`:

- **Primary/Text**: `var(--color-teal)` (#02433D)
- **Accents**: `var(--color-sage)`, `var(--color-beige)`, `var(--color-mint)`, `var(--color-peach)`
- **Backgrounds**: `var(--color-bg-light)` (#FDFCF8) - avoid pure white unless necessary.

### 3. Spacing & Layout

- Prioritize "breathing room" in layouts. Use `var(--spacing-lg)` and `var(--spacing-xl)` to create separation between sections.
- Use `section-padding` classes for consistency.

### 4. Tone of Voice

- Copy should be soothing, intentional, and inviting ("Come for what you need, stay for what you didn't know you were missing").
- Avoid aggressive marketing language.

## Code Style

- **HTML**: Semantic HTML5 tags (`<main>`, `<section>`, `<article>`).
- **CSS**:
  - Follow BEM (Block Element Modifier) naming conventions (e.g., `.card`, `.card__title`, `.card--featured`).
  - Use CSS variables for all design tokens (colors, spacing, radius).
  - Ensure responsive design, mobile-first approach.
