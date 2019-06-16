import React, {Component} from 'react';
import {Dimensions, ScrollView, Platform, StyleSheet, Text, View, AppRegistry, FlatList} from 'react-native';
import FormDiente from './Formulario';

const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;

/*

    Necesito que me entreguen:
        - el Json Dentadura (del paciente) (que tiene la info de cada diente del paciente)
            (se llama como data en el flatlist)
        - los valores del tratamiento como props
            (que se llaman en la clase FichaTratamiento)

*/

class ResumenDiente extends Component{
    render(){
        return(
        <View style={{justifyContent:'center', alignItems: 'center', margin: 20, flex:1,backgroundColor:'midnightblue'}}>
            <View style={{flex:1 ,flexDirection: 'column'}}>
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
                    <View style={{justifyContent:'center', alignItems: 'center', margin: 5}}>
                        <FormDiente
                            idDiente={this.props.idDiente}
                            tipoDiente={this.props.tipoDiente}
                            estadoDiente={this.props.estadoDiente}
                            comentarioDiente={this.props.comentarioDiente}
                        />
                    </View>
                </View>
            </View>
        </View>
        );
    }
}

export default class FichaTratamiento extends Component{
    render(){
        return(

            <View style= {{flex: 1}}>
                <View style={{flexDirection: 'column'}}>

                    <View style={{justifyContent:'center', alignItems: 'center'}}>
                        <Text style={{color:'midnightblue',marginTop: 10, fontSize : 0.08*SCREEN_WIDTH, fontWeight: 'bold'}}>
                            Ficha de Tratamiento
                        </Text>
                    </View>

                    <View style={{justifyContent:'center', flexDirection: 'column', margin: 10,backgroundColor:'midnightblue'}}>
                        <View>
                            <Text> Usuario: {this.props.Paciente}</Text>
                        </View>

                        <View>
                            <Text> Tipo de Tratamiento: {this.props.tipoTratamiento} </Text>
                        </View>

                        <View>
                            <Text> Vigencia: {this.props.estadoTratamiento}</Text>
                        </View>

                        <View>
                            <Text> Fecha de inicio: {this.props.inicioTratamiento}</Text>
                        </View>

                        <View>
                            <Text> Descripcion: {this.props.descripcionTratamiento}</Text>
                        </View>
                    </View>

                </View>

                <View style={{flex:1, flexDirection: 'row'}}>
                    <ScrollView>
                        <FlatList>
                            /* aqui se llama al JSON Dentadura, lo que
                            no se es si se puede modificar el texto dentro del json,
                            si es asi, entonces todo lo de adentro funciona bien.*/

                            data={this.props.Dentadura}
                            renderItem={({diente}) =>
                                <ResumenDiente {item.key}
                                    idDiente={diete.idDiente}
                                    tipoDiente={diete.tipoDiente}
                                    estadoDiente={diete.estadoDiente}
                                    comentarioDiente={diete.comentarioDiente}
                                />
                            }
                        </FlatList>
                    </ScrollView>
                </View>

            </View>


        );
    }
}