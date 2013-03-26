<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{title or 'Anmeldung für ZaPF'}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- style based on
      http://twitter.github.com/bootstrap/examples/marketing-narrow.html -->

    <!-- Le styles -->
    <link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
    </style>
    <link href="/static/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet">
    <link href="/static/css/web-anmeldung.css" rel="stylesheet">

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/bootstrap/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/bootstrap/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/bootstrap/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="/static/bootstrap/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="/static/bootstrap/ico/favicon.png">
  </head>

  <body>

    <div class="container-narrow">

      <div class="masthead">
        <ul class="nav nav-pills pull-right">
          <li {{!'class="active"' if home else ''}}><a href="/">Home</a></li>
          <li {{!'class="active"' if anmelden else ''}}><a href="/anmelden">Jetzt anmelden</a></li>
          <li><a href="http://www.zapf.uni-jena.de/" target="_blank">Mehr erfahren</a></li>
          <li><a href="http://www.fsr.uni-jena.de/index.php?option=com_contact&view=contact&id=4&Itemid=65&lang=de" target="_blank">Kontakt</a></li>
        </ul>
        <h3 class="muted">ZaPF SoSe 2013</h3>
      </div>

      <hr>

      %if home:
      <div class="jumbotron">
        <h1>Jetzt für die ZaPF in Jena anmelden!</h1>
        <p class="lead">Auf dieser Seite ist ab sofort die Anmeldung zu der Zusammenkunft aller Physik-Fachschaften im Sommersemester 2013 in Jena möglich.</p>
      </div>
      %end

      <div class="row-fluid marketing">
        <div class="span6">
          <center>
          <p>
            <img src="/static/images/zapf_tu-blau_klein.png" alt="ZaPF e.V. Logo" />
          </p>
          </center>
          <br />
          {{!additional_text or ""}}
        </div>

        <div class="span6">
          %include
        </div>
      </div>

      <hr>

      <div class="footer">
        <p>&copy; Die ZaPF 2013</p>
      </div>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/jquery/jquery-1.9.1.min.js"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script>

  </body>
</html>
