> Bulma spec
> MIT Licensed - CODENAME 2018

name: bulma
title: Bulma [partial] documentation from spec
version: 0.7.4
language: en
author: Arnaud Leymet
homepage: https://bulma.io
stylesheet: https://unpkg.com/bulma@0.7.4/css/bulma.min.css
description: Everything you need to create a website with Bulma


> reusable global modifiers

main colors:
- is-primary
- is-link
- is-info
- is-success
- is-warning
- is-danger

size helpers:
- is-small
- is-medium
- is-large

float:
- is-clearfix
- is-pulled-left
- is-pulled-right

spacing:
- is-marginless
- is-paddingless

other:
- is-overlay
- is-clipped
- is-radiusless
- is-shadowless
- is-unselectable
- is-invisible
- is-sr-only

responsive helpers:
- is-block
- is-flex
- is-inline
- is-inline-block
- is-inline-flex
- is-block-mobile
- is-block-tablet-only
- is-block-desktop-only
- is-block-widescreen-only
- is-block-touch
- is-block-tablet
- is-block-desktop
- is-block-widescreen
- is-block-fullhd
- is-flex-mobile
- is-flex-tablet-only
- is-flex-desktop-only
- is-flex-widescreen-only
- is-flex-touch
- is-flex-tablet
- is-flex-desktop
- is-flex-widescreen
- is-flex-fullhd
- is-inline-mobile
- is-inline-tablet-only
- is-inline-desktop-only
- is-inline-widescreen-only
- is-inline-touch
- is-inline-tablet
- is-inline-desktop
- is-inline-widescreen
- is-inline-fullhd
- is-inline-block-mobile
- is-inline-block-tablet-only
- is-inline-block-desktop-only
- is-inline-block-widescreen-only
- is-inline-block-touch
- is-inline-block-tablet
- is-inline-block-desktop
- is-inline-block-widescreen
- is-inline-block-fullhd
- is-inline-flex-mobile
- is-inline-flex-tablet-only
- is-inline-flex-desktop-only
- is-inline-flex-widescreen-only
- is-inline-flex-touch
- is-inline-flex-tablet
- is-inline-flex-desktop
- is-inline-flex-widescreen
- is-inline-flex-fullhd
- is-hidden-mobile
- is-hidden-tablet-only
- is-hidden-desktop-only
- is-hidden-widescreen-only
- is-hidden-touch
- is-hidden-tablet
- is-hidden-desktop
- is-hidden-widescreen
- is-hidden-fullhd

text color:
- has-text-white
- has-text-black
- has-text-light
- has-text-dark
- has-text-primary
- has-text-info
- has-text-link
- has-text-success
- has-text-warning
- has-text-danger
- has-text-black-bis
- has-text-black-ter
- has-text-grey-darker
- has-text-grey-dark
- has-text-grey
- has-text-grey-light
- has-text-grey-lighter
- has-text-white-ter
- has-text-white-bis

background color:
- has-background-white
- has-background-black
- has-background-light
- has-background-dark
- has-background-primary
- has-background-info
- has-background-link
- has-background-success
- has-background-warning
- has-background-danger
- has-background-black-bis
- has-background-black-ter
- has-background-grey-darker
- has-background-grey-dark
- has-background-grey
- has-background-grey-light
- has-background-grey-lighter
- has-background-white-ter
- has-background-white-bis

typo size:
- is-size-$*7

responsive size:
- is-size-$*7-mobile
- is-size-$*7-tablet
- is-size-$*7-touch
- is-size-$*7-desktop
- is-size-$*7-widescreen
- is-size-$*7-fullhd

alignment:
- has-text-centered
- has-text-justified
- has-text-left
- has-text-right

responsive alignment:
- has-text-centered-mobile
- has-text-centered-tablet
- has-text-centered-tablet-only
- has-text-centered-touch
- has-text-centered-desktop
- has-text-centered-desktop-only
- has-text-centered-widescreen
- has-text-centered-widescreen-only
- has-text-centered-fullhd
- has-text-justified-mobile
- has-text-justified-tablet
- has-text-justified-tablet-only
- has-text-justified-touch
- has-text-justified-desktop
- has-text-justified-desktop-only
- has-text-justified-widescreen
- has-text-justified-widescreen-only
- has-text-justified-fullhd
- has-text-left-mobile
- has-text-left-tablet
- has-text-left-tablet-only
- has-text-left-touch
- has-text-left-desktop
- has-text-left-desktop-only
- has-text-left-widescreen
- has-text-left-widescreen-only
- has-text-left-fullhd
- has-text-right-mobile
- has-text-right-tablet
- has-text-right-tablet-only
- has-text-right-touch
- has-text-right-desktop
- has-text-right-desktop-only
- has-text-right-widescreen
- has-text-right-widescreen-only
- has-text-right-fullhd

text transformation:
- is-capitalized
- is-lowercase
- is-uppercase
- is-italic

text weight:
- has-text-weight-light
- has-text-weight-normal
- has-text-weight-semibold
- has-text-weight-bold


# Columns

  ## Columns

  desc: Flexbox-powered responsive columns

  dom: .columns>.column

  ### examples

  default: .columns>(.column>.notification.is-primary{First column})+(.column>.notification.is-primary{Second column})+(.column>.notification.is-primary{Third column})+(.column>.notification.is-primary{Fourth column})

  gap:
  | If you want to remove the space between the columns, add the is-gapless modifier on the columns container.

  multi:
  | You can combine it with the is-multiline modifier.

  alignment:
  | While you can use empty columns (like <div class="column"></div>) to create horizontal space around .column elements,
  | you can also use .is-centered on the parent .columns element.

  ### modifiers

  gap:
  - is-gapless

  multi:
  - is-multiline

  alignment:
  - is-centered

  ## Column

  dom: .column

  ### examples

  default: .columns>(.column>.notification.is-primary{Column})

  ### modifiers

  sizes:
  - is-three-quarters
  - is-two-thirds
  - is-half
  - is-one-third
  - is-one-quarter
  - is-full
  - is-four-fifths
  - is-three-fifths
  - is-two-fifths
  - is-one-fifth
  - is-$@2*12
  - is-narrow
  - is-narrow-mobile
  - is-narrow-tablet
  - is-narrow-touch
  - is-narrow-desktop
  - is-narrow-widescreen
  - is-narrow-fullhd

  offset:
  - is-offset-three-quarters
  - is-offset-two-thirds
  - is-offset-half
  - is-offset-one-third
  - is-offset-one-quarter
  - is-offset-full
  - is-offset-four-fifths
  - is-offset-three-fifths
  - is-offset-two-fifths
  - is-offset-one-fifth
  - is-offset-$@2*12

  responsive < responsive helpers
  - is-mobile
  - is-tablet
  - is-desktop
  - is-widescreen
  - is-fullhd


# Layout

  ## Container

  dom: .container

  parents:
  - .navbar
  - .hero
  - .section
  - .footer

  ### examples

  default: .container>.notification{Container content.}

  fluid:
  | If you don't want to have a maximum width but want to keep the 32px margin on the left and right sides, add the is-fluid modifier.

  responsive:
  | With the two modifiers .is-widescreen and .is-fullhd, you can have a fullwidth container until those specific breakpoints.

  style:
  | If you don't want to see an arrow on on the side of the navbar, add the is-arrowless modifier.

  ### modifiers

  fluid:
  - is-fluid

  responsive:
  - is-mobile
  - is-tablet
  - is-desktop
  - is-widescreen
  - is-fullhd

  style:
  - navbar:is-arrowless

  ## Level

  dom:
  - nav.level>.level-item
  - nav.level>.level-left>.level-item
  - nav.level>.level-right>.level-item

  ### examples

  default: nav.level>.level-left>.level-item>p.subtitle.is-5>strong{123}^posts^^.level-item>.field.has-addons>p.control>input.input[placeholder={Find a post}]^p.control>button.button{Search}

  responsive:
  | By default, for space concerns, the level is vertical on mobile. If you want the level to be horizontal on mobile as well,
  | add the is-mobile modifier on the level container.

  ### modifiers

  responsive:
  - is-mobile

  ## Media Object

  dom:
  - article.media>.media-content
  - article.media>figure.media-left+.media-content
  - article.media>.media-content+.media-right
  - article.media>figure.media-left+.media-content+.media-right

  ### examples

  default: article.media>figure.media-left>p.image.is-64x64>img[src=https://bulma.io/images/placeholders/128x128.png]^^.media-content>.content>p>strong{John Smith }+small{@john 31m}+br+{Lorem ipsum dolor sit amet}

  ## Hero

  dom:
  - section.hero>.hero-body
  - section.hero>.hero-head+.hero-body+.hero-foot

  ### examples

  default: section.hero.is-primary>.hero-body>.container>h1.title{Hero title}+h2.subtitle{Hero subtitle}

  colors:
  | As with buttons, you can choose one of the 7 different colors.

  gradients:
  | By adding the is-bold modifier, you can generate a subtle gradient.

  sizes:
  | You can have even more imposing banners by using one of 3 different sizes.

  ### modifiers

  colors:
  - is-primary
  - is-info
  - is-success
  - is-warning
  - is-danger
  - is-light
  - is-dark

  gradients:
  - is-bold

  sizes:
  - is-medium
  - is-large
  - is-fullheight
  - is-fullheight-with-navbar

  ## Section

  dom:
  - body>section.section
  - main>section.section

  ### examples

  default: section.section

  ### modifiers

  spacing:
  - is-medium
  - is-large

  ## Footer

  dom: footer.footer

  ### examples

  default: footer.footer{Footer content}

  ## Tile

  dom:
  - .tile.is-ancestor>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile>.tile>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile>.tile>.tile>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile>.tile>.tile>.tile>.tile.is-parent>.tile.is-child
  - .tile.is-ancestor>.tile>.tile>.tile>.tile>.tile>.tile>.tile.is-parent>.tile.is-child

  ### examples

  default: .tile.is-ancestor>.tile.is-vertical.is-8>.tile>.tile.is-parent.is-vertical>article.tile.is-child.notification.is-primary{Tile #1}+article.tile.is-child.notification.is-warning{Tile #2}^.tile.is-parent>article.tile.is-child.notification.is-info{Tile #3}

  ### modifiers

  context:
  - is-ancestor
  - is-parent
  - is-child

  direction:
  - is-vertical

  size:
  - is-$*12


# Elements

  ## Box

  dom: .box

  ### examples

  default: .box>article.media>.media-left>figure.image.is-64x64>img[src='https://bulma.io/images/placeholders/128x128.png']^^.media-content>.content>p>strong{John Smith }+small{@johnsmith 31m}

  ## Button

  dom:
  - a.button
  - button.button
  - input:submit.button
  - input:reset.button

  ### examples

  default: a.button{Button}

  colors:
  | Colored buttons.

  sizes:
  | Size matters.

  outlined:
  | Outlined.

  inverted:
  | Inverted.

  rounded:
  | Rounded.

  loading:
  | Loading

  ### modifiers

  colors < main colors
  - is-white
  - is-light
  - is-dark
  - is-black
  - is-text

  sizes < size helpers

  outlined:
  - is-outlined

  inverted:
  - is-inverted

  rounded:
  - is-rounded

  loading:
  - is-loading

  ## Content

  dom:
  - .content>p
  - .content>ul
  - .content>ol
  - .content>dl
  - .content>h1
  - .content>h2
  - .content>h3
  - .content>h4
  - .content>h5
  - .content>h6
  - .content>blockquote
  - .content>em
  - .content>strong
  - .content>table
  - .content>ol

  ### examples

  default: .content>ol>li{Coffee}+li{Tea}+li{Milk}

  sizes:
  | You can use the is-small, is-medium and is-large modifiers to change the font size.

  ### modifiers

  sizes < size helpers

  ## Delete

  dom:
  - a.delete
  - button.delete

  parents:
  - span.tag
  - .notification
  - article.message.message-header

  ### examples

  default: a.delete

  sizes:
  | It comes in 4 sizes.

  ### modifiers

  sizes < size helpers

  ## Icon

  dom: span.icon>i

  ### examples

  default: span.icon>i.fas.fa-home

  colors:
  | Since icon fonts are simply text, you can use the text color modifiers to change the icon's color.

  sizes:
  | Size matters.

  ### modifiers

  colors < main colors

  sizes < size helpers

  ## Image

  dom: figure.image>img[src]

  ### examples

  default: figure.image>img[src=https://bulma.io/images/placeholders/128x128.png]

  ratio:
  | There are 7 dimensions to choose from, useful for avatars.

  rounded:
  | You can also make rounded images, using .is-rounded class.

  ### modifiers

  ratio:
  - is-square
  - is-1by1
  - is-5by4
  - is-4by3
  - is-3by2
  - is-5by3
  - is-16by9
  - is-2by1
  - is-3by1
  - is-4by5
  - is-3by4
  - is-2by3
  - is-3by5
  - is-9by16
  - is-1by2
  - is-1by3

  rounded:
  - is-rounded

  ## Notification

  desc: Bold notification blocks, to alert your users of something

  dom: .notification

  ### examples

  default: .notification>button.delete+{Lorem ipsum dolor sit amet.}

  colors:
  | Colored notifications.

  ### modifiers

  colors < main colors

  ## Progress bars

  desc: Native HTML progress bars.

  dom: progress.progress[val max]{nn %}

  ### examples

  default: progress.progress

  colors:
  | Colored progress bars.

  sizes:
  | Size matters.

  ### modifiers

  colors < main colors
  sizes < size helpers

  ## Table

  desc: The inevitable HTML table, with special case cells.

  dom: table.table>tbody>tr

  ### examples

  default: table.table>thead>tr>th{Pos}+th{Pts}^^tfoot>tr>th{Pos}+th{Pts}^^tbody>tr>th{1}+td{Leicester City}+td{81}

  bordered:
  | Add borders to all the cells.

  striped:
  | Add stripes to the table.

  narrow:
  | Make the cells narrower.

  hoverable:
  | You can add a hover effect on each row.

  fullwidth:
  | You can have a fullwidth table.

  ### modifiers

  bordered:
  - is-bordered

  striped:
  - is-striped

  narrow:
  - is-narrow

  hoverable:
  - is-hoverable

  fullwidth:
  - is-fullwidth

  ## Tag

  desc: Small tag labels to insert anywhere

  dom:
  - span.tag
  - a.tag

  ### examples

  default: span.tag{Tag label}

  colors:
  | Like with buttons, there are 10 different colors available.

  sizes:
  | And 2 additional sizes.

  rounded:
  | You can add the is-rounded modifier to make a rounded tag.

  delete:
  | You can add the is-delete modifier to turn the tag into a delete button.

  ### modifiers

  colors < main colors
  - is-black
  - is-dark
  - is-light
  - is-white

  sizes:
  - is-medium
  - is-large

  rounded:
  - is-rounded

  delete:
  - is-delete

  ## Tags

  desc: List of tags

  dom: .tags>.tag

  ### examples

  default: .tags>span.tag{One}+span.tag{Two}+span.tag{Three}

  ### modifiers

  sizing:
  - are-large
  - are-medium
  - are-small

  addons:
  - has-addons

  ## Title

  desc: Simple headings to add depth to your page

  dom:
  - h1.title
  - h$*6.title.is-$*6
  - h2.subtitle
  - h$*6.subtitle.is-$*6

  ### examples

  default: h1.title{Title}

  spaced:
  | You can maintain the normal spacing between titles and subtitles if you use the is-spaced modifier on the first element.

  ### modifiers

  spaced:
  - is-spaced


# Components

  ## Card

  desc: An all-around flexible and composable component

  dom: .card>(header.card-header>p.card-header-title{title})+(.card-image>figure.image)+(.card-content>p{content})+(footer.card-footer>.card-footer-item)

  ### examples

  default: .card>(header.card-header>p.card-header-title{title})+(.card-image>figure.image)+(.card-content>p{content})+(footer.card-footer>.card-footer-item)

  ## Tabs

  desc: Simple responsive horizontal navigation tabs, with different styles

  dom: .tabs>ul>.is-active{tab}

  ### examples

  default: .tabs>ul>li.is-active>a{Pictures}^li>a{Music}^li>a{Documents}

  alignment:
  | To align the tabs list, use the is-centered or is-right modifier on the .tabs container.

  sizes:
  | You can choose between 3 additional sizes ; is-small is-medium and is-large.

  styles:
  | Stylised tabs.

  ### modifiers

  alignment:
  - is-centered
  - is-right

  sizes < size helpers

  styles:
  - is-boxed
  - is-toggle
  - is-toggle-rounded
  - is-fullwidth
