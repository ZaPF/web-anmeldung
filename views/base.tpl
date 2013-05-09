<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{title + ' | ZaPF in Jena: SoSe 2013' if title else 'ZaPF in Jena: SoSe 2013'}}</title>
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
                                   <link rel="shortcut icon" href="/static/images/zapf_favicon.ico">
  </head>

  <body>

    <div class="container-narrow">

      <div class="masthead">
        <ul class="nav nav-pills pull-right">
          <li {{!'class="active"' if home else ''}}><a href="/">Home</a></li>
          %if not get('closed', True):
          <li {{!'class="active"' if anmelden else ''}}><a href="/anmelden">Jetzt anmelden</a></li>
          %end
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

      %include

      <hr>

      <div class="footer">
        <p>&copy; Die ZaPF 2013      |     <a href="https://github.com/ZaPF/web-anmeldung">ZaPF Web-Anmeldungs Projekt auf Github</a></p>
      </div>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/jquery/jquery-1.9.1.min.js"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script>
  <!-- Piwik -->
  <script type="text/javascript">
    var _paq = _paq || [];
    _paq.push(["trackPageView"]);
    _paq.push(["enableLinkTracking"]);
  
    (function() {
      var u=(("https:" == document.location.protocol) ? "https" : "http") + "://piwik.zapfev.de/";
      _paq.push(["setTrackerUrl", u+"piwik.php"]);
      _paq.push(["setSiteId", "3"]);
      var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0]; g.type="text/javascript";
      g.defer=true; g.async=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
    })();
  </script>
  <!-- End Piwik Code -->
  </body>
</html>
