import React, {Component} from 'react';
import {Button, FlatList, Image, StyleSheet, Text, View} from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';

import FichaTratamiento from './Tratamiento';

//Cambiar este User defecto por el JSON respectivo que le corresponde
const User = {
  nombre: 'Juanito',
  apellido_paterno: 'Alcachofa',
  apellido_materno: null,
  paciente: 'Juanito Alcachofa',
  rut: '12345678-9',
  sexo: 'Masculino',
  fecha_de_nacimiento: '29/02/2001',
  diagnosticado: true,
  tipoTratamiento: 'Tipo de tratamiento 1',
  estadoTratamiento: 'Estado de tratamiento 2',
  inicioTratamiento: 'Inicio de tratamiento 3',
  descripcionTratamiento: 'Descripcion de tratamiento 4',
  validado: true
};

class FichaPaciente extends Component {
	render() {
		return(
          	<View style={{flex: 1}}>
				<View style={{flex: 2, backgroundColor: 'darkturquoise', flexDirection: 'row'}}>
					<View style={{flex: 1}}>
						<Image source= {require('./images/pacienteficha.png')} style={{width: 80, height: 80}} />
					</View>
					<View style={{flex: 4,  alignItems: 'flex-end'}}>
						<Text style={{fontSize:24}}> {User.paciente} </Text>
						<Text style={{fontSize:18}}> Rut: {User.rut} </Text>
						<Text style={{fontSize:18}}> Edad: 18 </Text>
					</View>
				</View>
				<View style={{flex: 10, backgroundColor: 'turquoise', flexDirection: 'row'}}>
					<View style={{flex: 1, backgroundColor: 'cyan'}}>
						<Button
				          title="Revisar último tratamiento"
				          onPress={() => this.props.navigation.navigate('UltimoTratamiento', User)}
				        />
				        <Button
				          title="Revisar tratamientos anteriores"
				        />
					</View>
				</View>
			</View>
		);
	}
}

const styles = StyleSheet.create({
  item: {
    padding: 1,
    fontSize: 18,
    height: 44,
  },
})

//Navegador a tratamientos
const RootStack = createStackNavigator(
  {
    Home: FichaPaciente,
    UltimoTratamiento: FichaTratamiento,
  },
  {
    initialRouteName: 'Home',
  }
);

const AppContainer = createAppContainer(RootStack);

export default class App extends React.Component {
  render() {
    return <AppContainer />;
  }
}
