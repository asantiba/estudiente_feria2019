import React from 'react';
import { Button, Image, View, Text } from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';
//De aqui en adelante, agregar las views
import ModeloDental from './ModeloDent';
import ModalDiente from './modal';
import axios from 'axios';

class HomeScreen extends React.Component {
  

  constructor(props) {
    super(props);
    this.state = {
      nombre: '',
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
  render() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Image source={require('./images/Logo.jpg')} style={{height: '55%', width: '100%'}}/>
        <Button
          title= 'Ver Modelo'
          onPress={() => this.props.navigation.navigate('Modelo')}
        />
        <Button
          title="Ver Ficha (Work in Progress)"
          onPress={() => this.props.navigation.navigate('Modelo')}
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

