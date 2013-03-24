<h4>Anmeldeformular</h4>

<form method="POST">

  <label>Vorname:</label>
  <input type="text" id="first_name" name="first_name" placeholder="Ruppert" required>

  <label>Nachname:</label>
  <input type="text" id="last_name" name="last_name" placeholder="Weinrich" required>

  <label>E-Mail Adresse:</label>
  <input type="email" id="email_addr" name="email_addr" required title="Bitte g&uuml;ltige E-Mail Adresse eingeben.">

  <label>Universit&auml;t:</label>
  <select id="university" name="university">
    <option value="p-c" selected> bitte w&auml;hlen </option> 
    <option value="n-i-l"> - nicht in Liste - </option> 
    <option value="FFM">Frankfurt am Main</option>
    <option value="J">Jena</option>
  </select>

  <label>Universit&auml;t (falls nicht in Liste):</label>
  <input type="text" id="university_alt" name="university_alt">

  <label>Ern&auml;hrung:</label>
  <select id="food" name="food">
    <option value="p-c" selected> bitte w&auml;hlen </option> 
    <option value="n-i-l"> - nicht in Liste - bitte bei Sonstiges angeben - </option> 
    <option value="fleisch">Ich esse Fleisch!</option>
    <option value="vegi">Ich bin eingefleischter Vegetarier!</option>
    <option value="nix">Ich esse nix!</option>
  </select>

  <label>Arbeitskreis W&uuml;nsche:</label>
  <input type="text" id="arbeitskreise" name="arbeitskreise">

  <label>Sonstige W&uuml;nsche:</label>
  <input type="text" id="notes" name="notes">

  <button type="submit" class="btn btn-large btn-success">F&uuml;r ZaPF anmelden</button>
</form>

<p>Nach der Anmeldung ist noch eine<br />Best&auml;tigung per E-Mail notwendig.</p>

%rebase layout title=None
