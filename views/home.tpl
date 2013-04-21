    %if get('closed', False):
        <p>Die Anmeldung ist nun geschlossen.<br />Wir freuen uns auf die ZaPF!</p>
    %else:
        <a class="catchbtn btn btn-large btn-success" href="/anmelden">Jetzt zur ZaPF anmelden</a>
    %end

%rebase layout title=None, additional_text=None, home=True, anmelden=False
