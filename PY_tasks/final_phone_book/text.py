menu= ['Hauptmenü',
             'Datei öffnen',
             'Datei speichern',
             'Alle Kontakte anzeigen',
             'Neuen Kontakt erstellen',
             'Kontakt suchen',
             'Kontakt bearbeiten',
             'Kontakt löschen',
             'Beenden']

menu_select = 'Menüpunkt auswählen: '

def input_error ():
    return f'Falsche Eingabe. Wählen Sie eine Option von 1 bis {len(menu)-1}'

def add_successful (name: str) -> str:
    return f'Kontakt {name} erfolgreich hinzugefügt! Speichern Sie die Datei.'

input_contact = ['Kontaktname eingeben: ', 'Telefonnummer eingeben: ', 'Kommentar zum Kontakt eingeben: ']

input_change_contact = ['Neuen Namen eingeben: ', 'Neue Telefonnummer eingeben: ', 'Neuen Kommentar zum Kontakt eingeben: ']

load_successful = 'Die Datei wurde erfolgreich hochgeladen.'

empty_file = 'Telefonbuch ist leer oder Datei ist nicht geöffnet'

save_successful = 'Datei erfolgreich gespeichert'

not_found = 'Kontakt nicht gefunden'

input_index_delete = "Kontakt-ID zum Löschen eingeben: "

delete_successful = 'Kontakt erfolgreich gelöscht. Bitte Datei speichern.'

search_contact = 'Geben Sie den gesuchten Kontakt ein: '

input_index = 'Geben Sie die ID des Kontakts ein, den Sie ändern möchten (wenn Sie keine Änderungen vornehmen möchten, drücken Sie die Eingabetaste): '

edit_successful = 'Der Kontakt wurde erfolgreich geändert. Speichern Sie die Datei'

invalid_index = 'Der Index des Kontakts ist falsch'

delete_error = 'Fehler beim Löschen des Kontakts. Überprüfen Sie die eingegebene Nummer.'

message_exit = 'Bis später!'