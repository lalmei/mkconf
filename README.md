# mkconf

A simple mkdocs plugin to help create a simple static conference website.



Currently simply exposes the configuration to the mustache variables for the page templates. Feel free to contribute templates for each `needed` page. One can also make use of the `macros` [plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) to use the configuration variables within the markdown files,  though you might be limited on styling options.

## Motivation

Mkdocs yaml configs can be easily automated and created from csv's or excel files. Together with the mkdocs `mike` plugin and using CalVer-versioning one can easily keep track of a conference over the years with very little maintaince.


## Installation

`pip install mkconf`

and add it to the list of plugins in your mkdocs.yml file

```
plugins:
  - mkconf

```

## Usage 

you can pass the custom paths through the `speakers_file`, `organizers_file`, `agenda_file` parameters.

```
plugins:
  - mkconf
    - speakers_file: custom/path/to/file1.yml
    - organizers_file: custom/path/to/fil2.yml
    - agenda_file: custome/path/to/file3.yml
```

Otherwise it will use the `agenda.yml`, `speakers.yml`, and organizers.yml files in the root of your `mkdocs.yml` file.


## People

Both speakers, and organizers have the same schema, as a list of people objects. 

```
speakers:
    - name: "name1"
      title: "title1"
      company: "company1"
      image: /path/to/image1.jpg
      social_link: "https://linkedin.com/in/name1"
    - name: "name2"
      title: "title2"
      company: "company2"
      image: /path/to/image2.jpg
      social_link: "https://linkedin.com/in/name2"
```


## Agenda

The agenda follows the following schema.

```json
agenda:
  - range: ["8:00", "8:15"]
    display:
      h: 8
      m: ""
      a: "am"
    location: "Hall A"
    desc: "Opening Remarks & Welcome"

  - range: ["8:15", "9:45"]
    display:
      h: 8
      m: 15
      a: "am"
    location: "Hall B"
    desc: "Keynote Speech"

```

