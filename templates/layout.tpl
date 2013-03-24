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
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 720px;
      }
      .container-narrow > hr {
        margin: 30px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }
    </style>
    <link href="/static/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet">

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
          <li class="active"><a href="/">Home</a></li>
          <li><a href="http://www.zapf.uni-jena.de/">Mehr erfahren</a></li>
          <li><a href="http://www.fsr.uni-jena.de/index.php?option=com_contact&view=contact&id=4&Itemid=65&lang=de">Kontakt</a></li>
        </ul>
        <h3 class="muted">ZaPF SoSe 2013</h3>
      </div>

      <hr>

      <div class="jumbotron">
        <h1>Jetzt für ZaPF in Jena anmelden!</h1>
        <p class="lead">Auf dieser Seite ist ab sofort die Anmeldung zu der Zusammenkunft aller Physik-Fachschaften im Sommersemester 2013 in Jena möglich.</p>
      </div>

      <hr>

      <div class="row-fluid marketing">
        <div class="span6">
          <center>
            <img src="/static/images/zapf_tu-blau_klein.png" alt="ZaPF e.V. Logo" />
          </center>
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
