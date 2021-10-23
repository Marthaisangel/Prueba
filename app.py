from re import template
from flask import Flask, request, render_template, flash

import os

app = Flask(__name__)

#Martha

@app.route('/Asignar_Roles', methods=['GET', 'POST'])
def Asignar_Roles_Permisos():
    return render_template('Asignar_Roles_Permisos.html')

@app.route('/Cambiar_Contrasena_Pi', methods=['GET', 'POST'])
def Cambiar_Comtraseña_PI():
    return render_template('Cambiar_Contraseña_PI.html')

@app.route('/Cambiar_Contrasena_Sa', methods=['GET', 'POST'])
def Cambiar_Comtraseña_SA():
    return render_template('Cambiar_Contraseña_SA.html')

@app.route('/Cambiar_Contrasena_Us', methods=['GET', 'POST'])
def Cambiar_Comtraseña_US():
    return render_template('Cambiar_Contraseña_US.html')

@app.route('/CrearComentarios_Us', methods=['GET', 'POST'])
def Crear_Comentarios_US():
    return render_template('Crear_Comentarios_US.html')

@app.route('/CrearComentarios', methods=['GET', 'POST'])
def Crear_Comentarios():
    return render_template('Crearcomentarios.html')

@app.route('/CrearVuelo', methods=['GET', 'POST'])
def Crear_Vuelo():
    return render_template('CrearVuelo.html')

@app.route('/DashBoard_Pilotos', methods=['GET', 'POST'])
def DashBoard_Pilotos():
    return render_template('dashboard_Pilotos.html')

@app.route('/DashBoard_SA', methods=['GET', 'POST'])
def DashBoard_SA():
    return render_template('dashboardSA.html')

@app.route('/DashBoard_USU', methods=['GET', 'POST'])
def DashBoard_USU():
    return render_template('dashboardUSU.html')

#Jahan
@app.route('/Eliminarusuario', methods=['GET', 'POST'])
def Eliminar_Usuario():
    return render_template('Eliminar_Usuario.html')

@app.route('/EliminarvueloUS', methods=['GET', 'POST'])
def Eliminar_vuelo_US():
    return render_template('Eliminar_vuelo_US.html')

@app.route('/Eliminarvuelo', methods=['GET', 'POST'])
def Eliminar_vuelo():
    return render_template('Eliminar_vuelo.html')

@app.route('/Eliminarcomentarios', methods=['GET', 'POST'])
def Eliminar_comentarios():
    return render_template('eliminarcomentarios.html')

@app.route('/LoginSA', methods=['GET', 'POST'])
def loginSA():
    return render_template('loginSA.html')

@app.route('/Principal', methods=['GET', 'POST'])
def Principal():
    return render_template('Principal.html')

@app.route('/Registropiloto', methods=['GET', 'POST'])
def Registro_piloto():
    return render_template('Registro_Piloto.html')

@app.route('/Registrousuario', methods=['GET', 'POST'])
def Registro_usuario():
    return render_template('Registro_Usuario.html')

@app.route('/Reservavuelo', methods=['GET', 'POST'])
def reserva_vuelo():
    return render_template('Reservar_Vuelo.html')

@app.route('/PIvistacomentarios', methods=['GET', 'POST'])
def ver_comentarios_PI():
    return render_template('Ver_Comentarios_PI.html')


#Angie
@app.route('/SAvistacomentarios', methods=['GET', 'POST'])
def ver_comentarios_SA():
    return render_template('Ver_Comentarios_SA.html')

@app.route('/USvistacomentarios', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Comentarios_US.html')    

@app.route('/perfilpiloto', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Perfil piloto.html')   

@app.route('/perfilusuario', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Perfil Usuario.html')   

@app.route('/perfilSA', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Perfil_SA.html')   

@app.route('/verpilotos', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_pilotos.html')   

@app.route('/verusers', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Usuario.html')   

@app.route('/PIvervuelos', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Vuelos_PI.html')   

@app.route('/vervuelos', methods=['GET', 'POST'])
def ver_comentarios_US():
    return render_template('Ver_Vuelos.html')