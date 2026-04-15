---
title: "Publications"
layout: gridlay
excerpt: "Adam Rozman Publications PhD Candidate."
sitemap: true
permalink: /publications/
---


# Publication Highlights
Click a tile below to view the PDF or a page with more information.

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  {% if publi.click_redirect_page %}
    {% assign target_url = publi.click_redirect_page | relative_url %}
  {% else %}
    {% assign target_url = publi.link.url %}
  {% endif %}


<!-- <div class="well" style="border-radius: 0; cursor: pointer;" onclick="window.location.href='{{ target_url }}';"> -->
  <div class="well pub-tile" style="border-radius: 0; cursor: pointer;" onclick="window.location.href='{{ target_url }}';">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ publi.image }}" class="img-responsive" width="50%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>

  <p><strong>
    <a href="{{ publi.link.url }}" onclick="event.stopPropagation();">
    {% if publi.click_redirect_page %}
      {{publi.link.display }}
    {% else %}
      {{ publi.link.display }}
    {% endif %}
    </a>
  </strong></p>


  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Full List of publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}
