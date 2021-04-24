---
layout: page
title: Contribute
permalink: /contribute/
---


## Info on the recipe template

There is a
[sample recipe]
that fully uses the template.

This is mostly a documentation for me to use,
but if you want to try and submit your recipes in this format,
this page will be very helpful.

## Frontmatter

Jekyll makes heavy use of the
[frontmatter](https://jekyllrb.com/docs/front-matter/)
of a file.
From their docs:

> Any file that contains a YAML front matter block will be processed by Jekyll
> as a special file. The front matter must be the first thing in the file and
> must take the form of valid YAML set between triple-dashed lines. Here is a
> basic example:

```yaml
---
layout: post
title: Blogging Like a Pro
---
```

> Between these triple-dashed lines, you can set predefined variables  or even
> create custom ones of your own. These variables will then be available for
> you to access using Liquid tags both further down in the file and also in any
> layouts or includes that the page or post in question relies on.

I created a *lot* of custom values, that are automagically turned into a recipe.
This is quite nifty because I can use a single layout to build every recipe.

<!-- #### YAML format primer -->
<!-- TODO -->

## Recipe template

There are several sections in the template, let's walk through them.

### Preamble

Set basic information about you and the recipe:

```yaml
layout: recipe
category: dolci
author: Your name
title: A captivating title
serves: per 4 persone
excerpt: >
  A short description of the recipe, that will also be shown in the
  category page.
  Can be multiline, but will be rendered as a single paragraph.
```

* `layout`:
  Required.
  Has to be `recipe`, to tell Jekyll which layout to use.
* `category`:
  Required.
  The category this recipe will be filed in.
  One of
  [
  {%- for sorted_course in site.data.courses %}
      `{{ sorted_course.name }}`,
  {%- endfor -%}
  ].
* `serves`:
  Required.
  How many servings can be made with the doses listed in the ingredients.
  The entire field will be placed in parenthesis after the ingredients title.
* `excerpt`:
  Required.
  A short description of the recipe, that will also be shown in the category page.
  The `>` character allows for multi line content, do not remove it.

### Image of the finished result

You can show an image of the finised dish:

```yaml
imagefinished:
  filename: dolcetti_mandorle.jpeg
  alttext: A short description of the image content, for accessibility.
  caption: A caption for the image.
```

* `imagefinished`:
  Optional.
  An image to show the final result.
  - `filename`:
    Required.
    The filename with extension of the image.
  - `alttext`:
    Required.
    A short description of the image content, for accessibility.
  - `caption`:
    Optional.
    A caption for the image.

### Inspiration

If the recipe is *very* similar to someone else's,
give credit to the original author of the recipe.

```yaml
inspiration:
  name: Original Author Name
  text: >
    I'm so grateful to the author.
  link:
    url: https://www.example.com
    description: il suo fantastico blog
```

* `inspiration`:
  Optional.
  Where you got this recipe from.
  <!-- If it's on the internet, it's free. -->
  <!-- I'm not a lawyer. -->
  - `name`:
    Required.
    The name of the original author.
  - `text`:
    Optional.
    A paragraph describing the original recipe, why you like it, why you don't.
    What is your original contribution to the research.
    You know the drill.
  - `link`:
    Required.
    The link to the original recipe:
      - `url`:
      Required.
      The full url of the original recipe.
      - `description`:
      Required.
      A workaround for grammatical concordance between what you are linking
      and the description of it:
      it will be rendered as
      `Per maggiori informazioni visita {link.url.description}.`
      So in this example it would be:
      `Per maggiori informazioni visita il suo fantastico blog.`
      And the whole description will be the clickable part of the text.
      I mean, look at the [sample recipe] to see it in action,
      it is far clearer.

### Ingredient list

A composite ingredient list:

```yaml
ingredients:
  - preparation_name: null
    list:
    - name: Farina di mandorle
      quantity: 400g
    - name: Albumi
      quantity: 2
    - name: Zucchero
      quantity: tanto
    imageingredient:
      filename: dolcetti_mandorle/dolcetti_mandorle_ingredienti.jpg
      alttext: Ingredienti per i dolcetti di mandorle.
      caption: A caption for the image.
  - preparation_name: Per la glassa
    list:
    - name: Cioccolato
      quantity: 100g
```

* `ingredients`:
  Required.
  One or more lists of ingredients.
  - `preparation_name`:
    Required, can be `null` to skip the heading.
    The heading of the ingredient list being rendered.
  - `list`:
    Required.
    A list of ingredients for one preparation.
      - `name`:
      Required.
      The name of the ingredient.
      - `quantity`:
      Required.
      The quantity of the ingredient.
  - `imageingredient`:
    Optional.
    An image for the ingredient, one per preparation.
      - `filename`:
        Required.
        The filename with extension of the image.
      - `alttext`:
        Required.
        A short description of the image content, for accessibility.
      - `caption`:
        Optional.
        A caption for the image.

### Step list

A composite preparation steps list:

```yaml
steps:
  - preparation_name: null
    list:
    - type: text
      instruction: >
        Mescola tutto per bene.
    - type: text
      instruction: >
        Riposa.
    - type: image
      filename: dolcetti_mandorle.jpeg
      alttext: Un invitante foto di dolcetti alle mandorle.
  - preparation_name: Per la glassa
    list:
    - type: text
      instruction: >
        Sciogli il cioccolato a bagnomaria.
```

* `steps`:
  Required.
  One or more lists of steps.
  - `preparation_name`:
    Required, can be `null` to skip the heading.
    The heading of the step list being rendered.
  - `list`:
    Required.
    A list of steps for one preparation.
    There are two types of step: `text` and `image`,
    that can be freely mixed one after the other.
    1. `text` step:
      - `type`:
      Required.
      Must be set to `text`.
      - `instruction`:
      Required.
      The explanation for this step.
    1. `image` step:
      - `type`:
      Required.
      Must be set to `image`.
      - `filename`:
        Required.
        The filename with extension of the image.
      - `alttext`:
        Required.
        A short description of the image content, for accessibility.

### Notes

A simple list of notes.

```yaml
notes:
  - Ricordati lo zucchero a velo!
  - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua.
```

* `notes`:
  Optional.
  A  list of notes for the recipe.
  Mistically, there is no need for `>`. And apparently things do not break
  if I remove it from the other places, but who knows.

### See also

A list of related links.

```yaml
seealso:
  - text: >
      Questo link.
    link:
      url: https://www.youtube.com
      description: il suo canale youtube
  - text: >
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua.
    link:
      url: https://www.example.com
      description: il suo famoso blog
```

* `seealso`:
  Optional.
  A list of related resources.
  - `text`:
    Optional.
  - `link`:
    Required.
    The link to the additional resource:
      - `url`:
      Required.
      The full url of the page.
      - `description`:
      Required.
      A workaround for grammatical concordance between what you are linking
      and the description of it:
      Look at the [sample recipe] to see it in action.

<!-- Links -->
[sample recipe]: {{ "/samplerecipe/" | relative_url }}
