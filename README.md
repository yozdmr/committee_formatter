# Explanation
This project contains a python app that takes a `.docx` file containing information about the Farmer School Committees as input and produces HTML code used to update the [Farmer School Committees webpage](https://miamioh.edu/fsb/info-faculty-staff/committees.html) as output.

### The Input
The input must be formatted exactly as follows:
- The Committee categories must be **bold** and in *italics*.
  - `Standing` and `Ad Hoc`.
- The Committee names must be **bold** and <ins>underlined</ins>.
- All categories in a committee must be **bold** ONLY.
  - Chair, Members, Dean's Liaison, Committee Charge, etc.
- No text other than the types listed above should have bold. formatting.
- Ordered/unordered lists for things like committee charges are fine.

If these formatting criteria are not met, the HTML code output will not be correct.

### Committee JSON Storage Format
Example: The Academic Appeals Committee
```json
{
    "name": "Academic Appeals Committee",
    "chairs": [
        "EJ Ume (ECO) (2025)"
        ],
    "members": [
        "Geoff Zoeckler (ESP) (2026)"
	    "David Gempesaw (FIN) (2025)"
        "Michael Gowins (ISA) (2026)"
	    "Peter Nguyen (MKT) (2025)"	 
	    "Bill Moser (ACC) (2026)"
    ],
    "liaison": "Chanelle White",
    "alternates": [
        "Sydney Shu (ACC) (2026)"
        "Nam Vu (ECO) (2025)"
        "Chris Sutter (ESP) (2026)"
	    "Tyler Henry (FIN) (2025)"
	    "Vivian Chen (ISA) (2026)"
        "Darryl Rice (MGT) (2025)"
        "Eric Stenstrom (MKT) (2025)"
    ],
    "charge": [
        "Consider academic grievances as outlined in the Student Handbook."
        "The Committee will meet to address its annual charge. Meeting minutes will be taken."
        "The Committee Chair will provide a summative year-end report of Committee activities to the Associate Dean for Curriculum. This report will be added as a consent item to the agenda of the first faculty meeting of the following academic year.'
    ]
}
```
Any categories which do not appear in a committe will not exist in the JSON object. For example, the `alternates` category is not in every group, so it will only appear in the ones that do have it.

### Committee HTML Code Format
Example: The Academic Appeals Committee
```html
<p><strong>Chair</strong></p>
<p>EJ Ume (ECO) (2025)</p>
<p><strong>Dean's Liaison</strong></p>
<p>Chanelle White</p>
<p><strong>Members</strong></p>
<ul><li>Geoff Zoeckler (ESP) (2026)</li>
<li>David Gempesaw (FIN) (2025)</li>
<li>Michael Gowins (ISA) (2026)</li>
<li>Peter Nguyen (MKT) (2025)</li>
<li>Bill Moser (ACC) (2026)</li>
</ul><p><strong>Alternates</strong></p>
<ul><li>Sydney Shu (ACC) (2026)</li>
<li>Nam Vu (ECO) (2025)</li>
<li>Chris Sutter (ESP) (2026)</li>
<li>Tyler Henry (FIN) (2025)</li>
<li>Vivian Chen (ISA) (2026)</li>
<li>Darryl Rice (MGT) (2025)</li>
<li>Eric Stenstrom (MKT) (2025)</li>
</ul><p><strong>Committee Charge</strong></p>
<ol><li>Consider academic grievances as outlined in the Student Handbook.</li>
<li>The Committee will meet to address its annual charge. Meeting minutes will be taken.</li>
<li>The Committee Chair will provide a summative year-end report of Committee activities to the Associate Dean for Curriculum. This report will be added as a consent item to the agenda of the first faculty meeting of the following academic year.</li>
</ol>
```