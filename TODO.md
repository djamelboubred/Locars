# TODO

# to be done 

- [ ] HTML structure
    - [ ] Base -> DJAMS
        - [ ] Became Host
        - [ ] NavBar
            - [X] Structure
            - [X] Function click
            - [ ] Icons
            - [ ] Link page
                - [X] Login -> Djams
                    - [X] Register -> Djams
                    - [X] Logout -> Djams
                - [X] Profile
                    - [X] Shows profile picture
                        - [ ] Dell profile Picture
                    - [X] Modify information 
                        - [X] First Name
                        - [X] Last Name
                        - [X] Profile Picture
                    - [ ] Account 10/11 (vérifications des comptes dans la mise à jour 1.1)
                        - [X] Dell user
                        - [ ] Modify information of user
                            - [X] Adress
                            - [ ] Identy
                            - [X] Mail
                                - [ ] Verify you email
                            - [X] Phone number
                            - [ ] RIB ?
                    - [ ] Locarist
                        - [ ] First cars
                            - [ ] Id_Car for keys identification
                            - [ ] Adress
                            - [ ] Immatriculate (vérification des plaques d'immatriculation dans la mise à jour 1.2)
                            - [ ] Manual/automate
                        - [X] Add cars
                            - [X] Adress
                            - [X] Immatriculate
                            - [X] Manual/automate
                        - [ ] MyCars
                            - [X] Add cars
                            - [X] Details Cars
                            - [X] Dell cars
                    - [ ] Favories
                    - [ ] Travel
                    - [ ] Became Locarist
                        - [ ] if user.locarist == False
                        - [ ] else: no print this part
                    - [ ] Add cars
                        - [ ] My Cars
                        - [ ] Add Cars
                - [ ] Help
                - [ ] Tools for Host
                - [ ] Became Host
        - [ ] Footer
            - [ ] Contact
            - [ ] Help
            - [ ] Logo
            - [ ] Vehicule type
            - [ ] About
    - [ ] Home
    - [X] Login -> Djams
    - [X] Register -> Djams
    - [ ] Help -> FEFE
    - [ ] Cars
    - [X] Account
    - [ ] Became Host
        - [ ] my cars
        etc.
    
- [ ] Link between pages
    - [ ] Home
    - [ ] Login
    - [ ] Register
    - [ ] Help
    - [ ] Cars

- [ ] Function
    - [ ] search in home 
    - [ ] Login
        - [ ] verify information => with JavaScript
        - [X] redirect client in Account or Connection Pages after Connect
        - [ ] Send mail with gmail protocole
            - [ ] use no reply mail adress
        - [X] if user register authentificate pass connection page
        - [X] Use email or username for connection
        - [ ] Create link for verify your account
        - [X] create superUser -> Djams
            - [X] username => djams
            - [X] password => dianes
        - [ ] User
            - [X] email
            - [X] username
            - [X] first_name
            - [X] last_name
            - [X] phone_no
            - [X] profilePicture
            - [X] locarist (bolean)
            - [X] country
            - [X] city
            - [X] street
            - [ ] BirthDay
            - [ ] Permis or Identity Card

    date_creation = models.DateTimeField(auto_now_add=True)
    - [ ] add cars
    - [ ] Became Host

- [ ] Class/model
    - [ ] User
        - [ ] Travel
            - [ ] nb Travel
            - [ ] Travel Details
        - [ ] Favories
        - [ ] Locarist == False (DEFAULT)
    - [ ] Login
    - [ ] Cars
    - [ ] Comment
- [ ] Database
    - [ ] Pattern search
    - [ ] Filters





Mise à jour 1.1

Crypter donné
vérifier compte d'utilisateur avec permis, carte d'identité

