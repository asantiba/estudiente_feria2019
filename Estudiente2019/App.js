import React from 'react';
import { Button, Image, View, Text, Switch } from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';

//De aqui en adelante, agregar las views
import ModeloDental from './ModeloDent';
import ModalDiente from './modal';
import RegistroUsuario from './RegistroUsuario';
import FichaPaciente from './FichaPaciente';
import FichaBloqueada from './FichaBloqueada';
import axios from 'axios';


class HomeScreen extends React.Component {
  

  constructor(props) {
    super(props);
    this.state = {
      nombre: '',
	  permisoDado: false
    }
  }componentDidMount() {
    axios.get('http://192.168.43.212:8000/get_dientes') //tiene que ser TU ip
    .then(response => {
      alert(response.data[1].nombre); //aqui imprime el js obtenico
    })
    .catch(error => {
      console.log(error);
    });
  }
  
  // Para manejar el switch que entrega permiso:
  state = {permisoDado:false}
  toggleSwitch = (value) => {
      this.setState({permisoDado: value})
   }
  
  render() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Image source={require('./images/Logo.jpg')} style={{height: '55%', width: '100%'}}/>
        <Button
          title="Registrarse"
          onPress={() => this.props.navigation.navigate('Registro')}
        />
        <Button
          title="Revisar modelo dental"
          onPress={() => this.props.navigation.navigate('Modelo')}
        />
        <Button
          title="Ver Ficha"
          onPress={() => {
			if (this.state.permisoDado) {
			  this.props.navigation.navigate('Ficha')
			} else {
			  this.props.navigation.navigate('Bloqueada')
			}
		  }
		}
        />
		
		<View>
		<Text>
			{"\n"} {"\n"} {"\n"}
			Permitir ver Ficha
		</Text>
		<Switch 
		  onValueChange = {this.toggleSwitch}
          value = {this.state.permisoDado}
		/>
		</View>
		
      </View>
    );
  }
}

//Este es el "router"/navegador que dirige los nombres de las views



const RootStack = createStackNavigator(
  {
    Home: HomeScreen,
    Modelo: ModeloDental,
    Registro: RegistroUsuario,
    Ficha: FichaPaciente,
	Bloqueada: FichaBloqueada
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

