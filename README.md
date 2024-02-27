# mkconf

Simple mkdocs plugin to create a simple static conference website.
Currently simply exposes the configuration to the mustache variables for the page templates. Feel free to contribute templates for each `needed` page.

Mkdocs yaml configs can be easily automated and created from csv's or excel files. Together with the mkdocs `mike` plugin and using CalVer-versioning one can easily keep track of a conference over the years, with very little maintaince.



No page templates yet, but welcome contributions, it migth take me a while to get it done.

`pip install mkconf`

and add it to the list of plugins in your mkdocs.yml file

```
plugins:
  - mkconf

```
you can pass the custom paths through the `speakers_file, organizers_file, agenda_file`, 

```
plugins:
  - mkconf
    - speakers_file: custom/path/to/file1.yml
    - organizers_file: custom/path/to/fil2.yml
    - agenda_file: custome/path/to/file3.yml
```

otherwise It will use the agenda.yml, speakers.yml, and organizers.yml files in the root of your mkdocs.yml file.


## People

both speakers, and organizers are yml list of people items
Given by the following schema:

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

similarly for organizers:

```
organizers:
    - name:
      title:
      company:
      image:
      social_link:
```



