import React, {Component} from 'react';
import { View, StyleSheet, Button, ScrollView } from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';
import axios from 'axios';
import t from 'tcomb-form-native';


const Form = t.form.Form;
const User = t.struct({
	nombre : t.maybe(t.String),
	vigente: t.maybe(t.Number),
	fgen: t.maybe(t.Date),
	descripcion:t.maybe(t.String),
	descuento:t.maybe(t.String),
	garantias:t.maybe(t.String),
	resultados:t.maybe(t.String),
});

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

const options = {
  i18n: {
    optional: '',
    required: ' (*)',
  },
  fields: {
    fgen: {
      mode: 'date',
    },
  },
  stylesheet: formStyles,
};

export default class EditarFicha extends Component {
  handleSubmit = () => {
    const value = this._form.getValue();
    console.log('value: ', value);
    axios.post(
      'http://192.168.0.12:8000/update_tratamiento/', 
      {value}
  );
  alert('Actualizado');
  }

  render() {
    return (
      <ScrollView>
        <View style={styles.container}>
          <Form 
            ref={c => this._form = c}
            type={User} 
            options={options}
            value={{
            	nombre: null, 
            	vigente: null,
            	fgen: null,
            	descripcion: null,
            	descuento: null,
            	garantias: null,
            	resultados: null}}
          />
          <Button
            title="Actualizar"
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
