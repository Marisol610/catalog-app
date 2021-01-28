{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block content %}
<div class="container">
    <h3>Review Form</h3>
    <div class="col-sm-6">
        <form method="POST">
            {{wtf.quick_form(form) }}
        </form>
    </div>
</div>

{% endblock %}