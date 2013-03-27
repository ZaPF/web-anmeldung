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

  <label>Exkursionswunsch 1:</label>
  <select id="exkursion1" name="exkursion1">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}">{{exkursion.title}}</option>
    %end
  </select>

  <label>Exkursionswunsch 2:</label>
  <select id="exkursion2" name="exkursion2">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}">{{exkursion.title}}</option>
    %end
  </select>

  <label>Exkursionswunsch 3:</label>
  <select id="exkursion3" name="exkursion3">
    %for exkursion in exkursionen:
    <option value="{{exkursion.code}}">{{exkursion.title}}</option>
    %end
  </select>

  <label>Ernährung:</label>
  %for choice in essen:
    <label class="radio">
      <input type="radio" name="food" id="{{choice.code}}" value="{{choice.code}}" {{'checked' if choice.code == u'fleisch' else ''}}>
      {{choice.commitment}}
    </label>
  %end
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
