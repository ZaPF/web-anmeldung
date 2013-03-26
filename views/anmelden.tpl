<div id="anmeldeformular">
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
    %for uni in unis:
    <option value="{{uni.acronym}}">{{uni.name}}</option>
    %end
  </select>

  <label>Universität (falls nicht in Liste):</label>
  <input type="text" id="university_alt" name="university_alt">

  <label>Arbeitskreis Wünsche:</label>
  <input type="text" id="arbeitskreise" name="arbeitskreise">

  <label>Exkursionswunsch:</label>
  <select id="exkursion" name="exkursion">
    <option value="ex1">Exkursion 1</option>
    <option value="ex2">Exkursion 2</option>
    <option value="ex3">Exkursion 3</option>
  </select>

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

  <label>T-Shirt Größe:</label>
  <select id="tshirt" name="tshirt">
    <option value="xs">XS</option>
    <option value="s">S</option>
    <option value="m" selected>M</option>
    <option value="l">L</option>
    <option value="xl">XL</option>
    <option value="xxl">XXL</option>
    <option value="xxxl">XXXL</option>
  </select>

  <label>Sonstige Wünsche:</label>
  <textarea rows="3" id="notes" name="notes"></textarea>

  <button type="submit" class="btn btn-large btn-success">Für ZaPF anmelden</button>
</form>

</div>

%rebase layout title=None, additional_text="<h4>Information</h4><p>Der Tagungsbeitrag beträgt 25€ pro Person.</p><p>Nach der Anmeldung ist noch eine<br />Bestätigung per E-Mail notwendig.</p>", home=False, anmelden=True
