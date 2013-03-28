          <h4>Teilnehmer nach Universitäten</h4>
          <ul>
              %for uni in rbu.keys():
              <li>{{uni}}</li>
              <ul>
                  %for registrant in rbu[uni]:
                  <li>{{registrant['first_name'] + " " + registrant['last_name'][0] + "."}}</li>
                  %end
              </ul>
              %end
          </ul>

%rebase bare title=u"Anmeldungen nach Universität", additional_text=None, home=False, anmelden=False

