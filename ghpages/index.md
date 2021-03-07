---
title: Home
---

# Portate

{% for sorted_course in site.data.courses %}
{% for course in site.courses %}
{%- if course.short_name == sorted_course.name -%}

## [{{ course.title }}]({{ course.url | relative_url }})

{{ course.content }}

{%- endif -%}
{% endfor %}
{% endfor %}
