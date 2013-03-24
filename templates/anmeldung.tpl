<h4>Anmeldeformular</h4>

<form method="POST">

  <label>Vorname:</label>
  <input type="text" id="first_name" name="first_name" placeholder="Ruppert" required>

  <label>Nachname:</label>
  <input type="text" id="last_name" name="last_name" placeholder="Weinrich" required>

  <label>E-Mail Adresse:</label>
  <input type="email" id="email_addr" name="email_addr" required title="Bitte gültige E-Mail Adresse eingeben.">

  <label>Universität:</label>
  <select id="university" name="university">
    <option value="p-c" selected> bitte wählen </option> 
    <option value="n-i-l"> - nicht in Liste - </option> 
    <option value="FFM">Frankfurt am Main</option>
    <option value="J">Jena</option>
  </select>

  <label>Universität (falls nicht in Liste):</label>
  <input type="text" id="university_alt" name="university_alt">

  <label>Ernährung:</label>
  <label class="radio">
    <input type="radio" name="food" id="fleisch" value="fleisch" checked>
    Ich esse auch Fleisch.
  </label>
  <label class="radio">
    <input type="radio" name="food" id="vegi" value="vegi">
    Ich bin Vegetarier.
  </label>
  <br />

  <label>Arbeitskreis Wünsche:</label>
  <input type="text" id="arbeitskreise" name="arbeitskreise">

  <label>Sonstige Wünsche:</label>
  <input type="text" id="notes" name="notes">

  <button type="submit" class="btn btn-large btn-success">Für ZaPF anmelden</button>
</form>

<p>Nach der Anmeldung ist noch eine<br />Bestätigung per E-Mail notwendig.</p>

%rebase layout title=None
