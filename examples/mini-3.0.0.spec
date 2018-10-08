> Mini.css spec
> MIT Licensed - CODENAME 2018

name: mini
title: Mini.css [partial] documentation from spec
version: 3.0.0
language: en
author: Arnaud Leymet
homepage: https://minicss.org
stylesheet: https://unpkg.com/mini.css@3.0.0/dist/mini-default.min.css

-- description
minimal, responsive, style-agnostic CSS framework
-- description


> reusable global modifiers

global colors:
- primary
- secondary
- tertiary

global sizes:
- small
- large


> atomic elements

# Elements

  ## Button

  desc:
  | Buttons and button-like input elements have been styled by default to be consistent across browsers.
  | You can also style other elements, such as links or form labels, to look like buttons, using the appropriate class
  | (.button)or the button role.

  dom:
  - button
  - input:button
  - input:reset
  - input:submit
  - a.button
  - a[role=button]
  - label.button
  - label[role=button]

  ### examples

  default: button{Button}

  color variants:
  | To make your buttons stand out, you can give them a primary (.primary), secondary (.secondary),
  | tertiary (.tertiary) or inversed (.inverse) color palette.

  size variants:
  | You can make buttons smaller (.small) or larger (.large), by applying the appropriate modifier.

  ### modifiers

  color variants < global colors
  - inverse

  size variants < global sizes

  ## Image

  desc:
  | Image elements are responsive by default, automatically scaling down as necessary to display properly on smaller devices.
  | Images retain their original aspect ratio and they will never scale above their original size.
  | If you want to add captions to images, you can use HTML5 figure elements, along with their related captions.

  dom: figure>img+figcaption

  ### examples

  default: figure>img[src=https://placehold.it/800x600]+figcaption{image caption}


> components, elements assembled into molecules

# Components

  ## Card

  desc:
  | mini.css provides you with cards (.card), general-purpose containers that help you organize the content of your web apps.
  | Cards should be used in combination with the grid system, meaning that they need to be placed inside a grid's rows to work
  | properly. Layouts created with cards are responsive, realigning according to the available size on the screen.

  dom: .card

  ### examples

  default: .card>h3{Card}+p{This is a basic card with some sample content}

  alternative sizes:
  | You can create small (.small, 240px wide) or large (.large, 480px wide) cards by applying the appropriate modifiers
  | to a card. Apart from that, you can also create fluid (.fluid) cards, that take up as much space as is available,
  | however you will have to place these cards inside a grid layout's columns, effectively adding one extra step for them
  | to display properly.

  color variants:
  | You can display warning (.warning) or error (.error) messages using cards, simply by adding the appropriate color
  | modifiers to a card.

  ### modifiers

  alternative sizes < global sizes
  - fluid

  color variants:
  - warning
  - error
