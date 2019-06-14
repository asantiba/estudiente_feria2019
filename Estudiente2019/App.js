import React from 'react';
import { Button, Image, View, Text } from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';

//De aqui en adelante, agregar las views
import ModeloDental from './ModeloDent';
import ModalDiente from './modal';
import RegistroUsuario from './RegistroUsuario';
import FichaPaciente from './FichaPaciente';

class HomeScreen extends React.Component {

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
          onPress={() => this.props.navigation.navigate('Ficha')}
        />
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
