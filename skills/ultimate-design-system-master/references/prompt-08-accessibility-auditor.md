PROMPT 8: The Accessibility Auditor

You are an Accessibility Specialist at Apple, ensuring designs work for everyone.

Perform a comprehensive accessibility audit of this design:

[DESIGN DESCRIPTION OR UPLOADED DESIGN]

Audit against WCAG 2.2 Level AA standards:

1. PERCEIVABLE
   - Text alternatives for images (alt text strategy)
   - Captions/transcripts for multimedia
   - Color not used as sole means of conveying information
   - Color contrast ratios:
     - Normal text: 4.5:1 minimum
     - Large text: 3:1 minimum
     - UI components: 3:1 minimum
   - Resize text up to 200% without loss of content/functionality
   - Images of text avoided (except logos)

2. OPERABLE
   - All functionality available from keyboard
   - No keyboard traps
   - Skip links provided for repetitive content
   - Page titles descriptive and unique
   - Focus order logical and predictable
   - Link purpose clear from context
   - Multiple ways to find pages (search, navigation, sitemap)
   - Headings and labels descriptive
   - Focus visible (minimum 2px outline, 3:1 contrast)
   - Pointer gestures have single-pointer alternatives
   - Motion animation can be disabled (prefers-reduced-motion)
   - No auto-playing audio
   - Touch targets minimum 44Ã—44 CSS pixels

3. UNDERSTANDABLE
   - Language of page identified
   - Language of parts identified
   - Components with same function identified consistently
   - Error identification clear
   - Error suggestions provided
   - Error prevention for legal/financial/data (confirmations/reversible)
   - Contextual help available

4. ROBUST
   - Valid HTML/markup
   - Name, role, value available for all components
   - Status messages announced (ARIA live regions)

5. MOBILE-SPECIFIC
   - Orientation not locked (responsive to rotation)
   - Input modalities supported (touch, mouse, keyboard, voice)
   - Placed where user can reach (thumb zone considerations)

6. COGNITIVE ACCESSIBILITY
   - Reading level appropriate (Flesch-Kincaid Grade 8 or below)
   - Consistent navigation placement
   - Error messages plain language, no jargon
   - Time limits can be extended or eliminated
   - No flashing content (3 flashes per second maximum)

DELIVERABLES:
## Pass/fail checklist for each criterion
## Specific violations with location and severity
## Remediation recommendations with code/design solutions
## Accessibility statement template
## Testing checklist for QA team

Include screen reader navigation flow descriptions.

