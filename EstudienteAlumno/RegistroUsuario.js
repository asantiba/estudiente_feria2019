import React, {Component} from 'react';
import { View, StyleSheet, Button, ScrollView } from 'react-native';
import axios from 'axios';
import t from 'tcomb-form-native';
//Documentacion para este modulo en : https://github.com/gcanti/tcomb-form-native

//TO-DO : 
//Validacion de rut. 
//Cambiar el modo en el que se elije la fecha de nacimiento por un config{dialogmode: spinner} o algo asi

const Form = t.form.Form;

//Aqui se define el modelo del paciente, key-value
//Los 2 ultimos valores (diagnosticado y validado), son pasados como false por defecto y no son elegidos por el usuario
const User = t.struct({
  nombre: t.String,
  apellido_paterno: t.String,
  apellido_materno: t.String,
  rut: t.Number,
  correo: t.String,
  direccion: t.maybe(t.String),
  estado_civil: t.maybe(t.enums({S: 'Solter@', C: 'Casad@'})),
  sexo: t.enums({M: 'Masculino', F: 'Femenino', O: 'Otro'}),
  celular: t.Number,
  ocupacion: t.String,
  fecha_de_nacimiento: t.Date,
  terms: t.Boolean,
  diagnosticado: t.Boolean,
  validado: t.Boolean
});

//Configuraciones de estilo
const formStyles = {
  ...Form.stylesheet,
  formGroup: {
    normal: {
      marginBottom: 10
    },
  },
  controlLabel: {
    normal: {
      color: 'blue',
      fontSize: 18,
      marginBottom: 7,
      fontWeight: '600'
    },
    error: {
      color: 'red',
      fontSize: 18,
      marginBottom: 7,
      fontWeight: '600'
    }
  }
}

//Opciones de personalizacion del formulario
const options = {
  i18n: {
    optional: '',
    required: ' (*)',
  },
  fields: {
    fecha_de_nacimiento: {
      mode: 'date',
    },
    correo: {
      error: 'Sin un correo no podremos enviarte recuperaciones de tu cuenta en caso de pérdida.'
    },
    terms: {
      label: 'Aceptar términos y condiciones de servicio'
    },
    validado:{
      hidden: true
    },
    diagnosticado:{
      hidden: true
    }
  },
  stylesheet: formStyles,
};

//Al clickear el boton, los datos iran a 'value'.
//Trabajar en base a eso, por ahora, solo lo tira en consola (debugger)
//Pero a futuro debe guardarlos en la Base de datos.
export default class RegistroUsuario extends Component {
  handleSubmit = () => {
    const value = this._form.getValue();
    console.log('value: ', value);
    axios.post(
      'http://192.168.0.12:8000/post_paciente/', 
      {value}
  );
  alert('Registrado');
  }

  render() {
    return (
      <ScrollView>
        <View style={styles.container}>
          <Form 
            ref={c => this._form = c}
            type={User} 
            options={options}
            value={{diagnosticado: false, validado: false}}
          />
          <Button
            title="Registrarme"
            onPress={this.handleSubmit}
          />
        </View>
      </ScrollView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    marginTop: 50,
    padding: 20,
    backgroundColor: '#ffffff',
  },
});
