<h4>{{message_title or u"Information"}}</h4>

<div class="alert alert-success">
<i class="icon-check"></i>   <strong>{{alert}}</strong><br />
{{message}}
</div>

%rebase layout title=(message_title or u"Information"), additional_text=None, home=False, anmelden=False
