<div id="anmeldeformular">
%if error:
<h4> <span class="label label-important">! Fehler mit der Anmeldung</span> </h4>

<div class="alert alert-error">
{{error}}
</div>
%end
<h4>Anmeldeformular</h4>

<form method="POST">

  <label>Vorname:</label>
  <input type="text" id="first_name" name="first_name" value="{{registrant['first_name'] if error else ""}}" placeholder="Vorname" required>

  <label>Nachname:</label>
  <input type="text" id="last_name" name="last_name" value="{{registrant['last_name'] if error else ""}}" placeholder="Nachname" required>

  <label>E-Mail Adresse:</label>
  <input type="email" id="email_addr" name="email_addr" value="{{registrant['email'] if error else ""}}" placeholder="du@deine-uni.de" required title="Bitte gültige E-Mail Adresse eingeben.">

  <label>Spitzname:</label>
  <input type="text" id="nick_name" name="nick_name" value="{{registrant['nick_name'] if error else ""}}" placeholder="Spitzname">

  <label>Universität:</label>
  <select id="university" name="university">
    %for uni in unis:
    <option value="{{uni.acronym}}" {{"selected" if error and registrant['university'] == uni.acronym else ""}}>{{uni.name}}</option>
    %end
  </select>

  <label>Universität (falls nicht in Liste):</label>
  <input type="text" id="university_alt" name="university_alt" value="{{registrant['university_alt'] if error else ""}}">

  <label>Arbeitskreis Wünsche:</label>
  <input type="text" id="arbeitskreise" name="arbeitskreise" value="{{registrant['arbeitskreise'] if error else ""}}">

  <label>Exkursionswunsch 1:</label>
  <select id="exkursion1" name="exkursion1">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}" {{"selected" if error and registrant['exkursion1'] == exkursion.code else ""}}>{{exkursion.title}}</option>
    %end
  </select>

  <label>Exkursionswunsch 2:</label>
  <select id="exkursion2" name="exkursion2">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}" {{"selected" if error and registrant['exkursion2'] == exkursion.code else ""}}>{{exkursion.title}}</option>
    %end
  </select>

  <label>Exkursionswunsch 3:</label>
  <select id="exkursion3" name="exkursion3">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}" {{"selected" if error and registrant['exkursion3'] == exkursion.code else ""}}>{{exkursion.title}}</option>
    %end
  </select>

  <label>Ernährung:</label>
  %for choice in essen:
    <label class="radio">
      <input type="radio" name="food" id="{{choice.code}}" value="{{choice.code}}" {{'checked' if error and registrant['food'] == choice.code else ('checked' if not error and choice.code == u'fleisch' else '')}}>
      {{choice.commitment}}
    </label>
  %end
  <br />

  <label>T-Shirt Größe:</label>
  <select id="tshirt" name="tshirt">
    %for tshirt in tshirts:
        <option value="{{tshirt.code}}" {{'selected' if error and registrant['tshirt'] == tshirt.code else ('selected' if not error and tshirt.code == u'L-m' else '')}}>{{tshirt.name}}</option>
    %end
  </select>

  <label>Sonstige Wünsche:</label>
<textarea rows="3" id="notes" name="notes">{{registrant['notes'] if error else ""}}</textarea>

  <button type="submit" class="btn btn-large btn-success">Für ZaPF anmelden</button>
</form>

</div>

%rebase layout title="Jetzt anmelden", additional_text="<h4>Information</h4><p>Der Tagungsbeitrag beträgt 25€ pro Person.</p><p>Nach der Anmeldung ist noch eine<br />Bestätigung per E-Mail notwendig.</p>", home=False, anmelden=True
