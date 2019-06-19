import React, {Component} from 'react';
import {Button, Dimensions, ScrollView, Platform, StyleSheet, Text, View, AppRegistry, FlatList} from 'react-native';
import FormDiente from './Formulario';
import { createStackNavigator, createAppContainer } from 'react-navigation';
import axios from 'axios';


const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;

/*

    Necesito que me entreguen:
        - el Json Dentadura (del paciente) (que tiene la info de cada diente del paciente)
            (se llama como data en el flatlist)

*/

class ResumenDiente extends Component{
    render(){
        return(
        <View style={{justifyContent:'center', alignItems: 'center', margin: 20, flex:1,backgroundColor:'midnightblue'}}>
                <View style={{flexDirection: 'row'}}>
                    <View style={{margin: 30, marginTop: 5, marginBottom:5, justifyContent:'center', alignItems: 'center'}}>
                        <Text style={{color:'white', fontSize : 0.05*SCREEN_WIDTH, fontWeight: 'bold'}}>
                            Pieza {this.props.idDiente}
                        </Text>
                    </View>
                    <View style={{flex:1, flexDirection: 'column', justifyContent:'center'}}>
                        <View>
                            <Text style={{color:'white', fontSize : 0.04*SCREEN_WIDTH, fontWeight: 'bold'}}>
                                Tipo: {this.props.tipoDiente}
                            </Text>
                        </View>
                        <View>
                            <Text style={{color:'white', fontSize : 0.04*SCREEN_WIDTH, fontWeight: 'bold'}}>
                                Estado: {this.props.estadoDiente}
                            </Text>
                        </View>
                    </View>
                </View>
                <View style={{flexDirection: 'row'}}>
                    <View style={{margin:15, marginTop: 5, marginBottom:10, flex:1, borderColor: 'white'}}>
                        <Text style={{color:'white'}}>
                            Comentario: {this.props.comentarioDiente}.
                        </Text>
                    </View>
                    
                </View>
        </View>
        );
    }
}

export default class FichaTratamiento extends Component{
    constructor(props){
        super(props);
        this.state = {
            loading1: false,
            loading2: false,
            data: [],
            dicto: {},
            dic: {},
            error: null,
            refreshing: false,
        }
    }
    componentDidMount() {
        const self = this;
        axios.get('http://192.168.0.12:8000/get_tratamiento_by_paciente/1') //tiene que ser TU ip
        .then((response) => {
          this.setState({dictos:response.data});
          this.setState({loading1:true})
        })
        .catch(error => {
          console.log(error);
        });
        axios.get('http://192.168.0.12:8000/get_dentadura_by_paciente/189589145') //tiene que ser TU ip
        .then((response) => {
          this.setState({dics:response.data});
          this.setState({loading2:true});
        })
        .catch(error => {
          console.log(error);
        });
    }
    render(){
        //const { navigation } = this.props; //Esto es lo que recibe de hacer click en el boton "Revisar ultima ficha"
        var tratamientoUsuario = this.state.dictos;
        var Dentadura = this.state.dics;
        return(
            <View style= {{flex: 1}}>
                <View style={{flexDirection: 'column'}}>

                    <View style={{justifyContent:'center', alignItems: 'center'}}>
                        <Text style={{color:'midnightblue',marginTop: 10, fontSize : 0.08*SCREEN_WIDTH, fontWeight: 'bold'}}>
                            Ficha de Tratamiento
                        </Text>
                    </View>

                    <View style={{justifyContent:'center', flexDirection: 'column', margin: 10,backgroundColor:'cyan'}}>
                        {this.state.loading1 ?(
                        <View>
                            <Text> Tipo de Tratamiento: {tratamientoUsuario[0]["nombre"]} </Text>
                            {tratamientoUsuario[0]["vigente"] ? (
                                <Text> Vigencia: Si </Text>
                            ):( <Text> Vigencia: No </Text>)}
                            <Text> Fecha de inicio: {tratamientoUsuario[0]["fgen"]} </Text>
                            <Text> Descripcion: {tratamientoUsuario[0]["descripcion"]}</Text>
                            <Text> Descuento: {tratamientoUsuario[0]["descuento"]}</Text>
                            <Text> Garantias: {tratamientoUsuario[0]["garantias"]}</Text>
                            <Text> Resultados: {tratamientoUsuario[0]["resultados"]}</Text>
                        </View>
                        ):(<View></View>)}
                    </View>
                    <Button title="editar ficha"
                        onPress={() => this.props.navigation.navigate('EditarFicha')} />

                </View>
                <View style={{flex:1, flexDirection: 'row'}}>
                {this.state.loading2 ?(
                    <ScrollView> 
                        <FlatList
                            data={Dentadura}
                            renderItem={({item}) =>
                                <ResumenDiente
                                    //Arreglame
                                    idDiente={item.iddiente}
                                    tipoDiente={'incisivo central'}
                                    estadoDiente={item.estado}
                                    comentarioDiente={item.comentario_detallado}
                                />
                            }
                        />
                        
                    </ScrollView>
                    ):(<View></View>)}
                </View>
            </View>


        );
    }
}

