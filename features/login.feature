Feature: Login Functionality

Scenario: Username benar dan Password benar

Given User membuka halaman login
When User memasukkan username "tomsmith"
And User memasukkan password "SuperSecretPassword!"
And User menekan tombol login
Then User berhasil login


Scenario: Username benar dan Password salah

Given User membuka halaman login
When User memasukkan username "tomsmith"
And User memasukkan password "PasswordSalah"
And User menekan tombol login
Then User gagal login