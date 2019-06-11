import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image } from 'react-native';
import {Modal, TouchableHighlight, Alert, TouchableOpacity} from 'react-native';


export default class ModalDiente extends Component {
  state = {
    modalVisible: false,
  };
  setModalVisible(visible) {
    this.setState({modalVisible: visible});
  }

  render() {
    let pic = {
          uri: './images/placeholder.png'
        };
    return (
      <View style={{marginTop: 22}}>
        <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => {this.setModalVisible(!this.state.modalVisible)}}>
          <View style={{flex: 1, backgroundColor: '#f0f8ff'}}>
            <View  style={{flex: 1, marginTop: 22, margin:10, marginBottom:10, backgroundColor:'lightskyblue'}}>


                <View style={{flexDirection: 'row',  margin:10}}>

                    <Image source={require('./images/placeholder.png')} style={{width: 200, height: 200}}/>

                    <View style={{flex: 1, margin:5,marginTop:0, marginBottom:0, flexDirection: 'column', backgroundColor: '#f0f8ff'}}>
                        <View style={{justifyContent: 'center'}} >
                            <Text style={{fontWeight: 'bold', color:'midnightblue',  fontSize: 12}}>
                                Pieza n° X
                            </Text>
                        </View>
                    </View>
                </View>


                <View style={{flex: 1, marginTop: 10, margin:10,}}>
                    <Text style={{fontWeight: 'bold', color:'midnightblue',  fontSize: 20}}>
                        Informacion:
                    </Text>
                    <View style={{flex: 1, backgroundColor: '#f0f8ff', marginTop: 5}}>
                        <View style={{margin: 10 , marginBottom:3}}>
                            <ScrollView >
                                <View style={{height: 500, backgroundColor: 'orange'}} />
                                <View style={{height: 500, backgroundColor: '#f0f8ff'}} />
                            </ScrollView>
                        </View>
                    </View>
                </View>

                <View style={{height: 50, margin: 30,marginBottom:10,marginTop:5, backgroundColor: 'orange'}}>
                       <TouchableOpacity
                       onPress={() => {this.setModalVisible(!this.state.modalVisible);}}
                       style={{justifyContent:'center', alignItems: 'center'}}>
                           <Text style={{color: '#f0f8ff',
                           fontWeight: 'bold',
                           fontSize: 30}}>
                              Entendido
                           </Text>
                       </TouchableOpacity>
                </View>
            </View>
          </View>
        </Modal>


        <TouchableHighlight
          onPress={() => {
            this.setModalVisible(true);
          }}
          style={{width: 193, height: 110,}}>
              <Image source={require('./images/placeholder.png')} style={{width: 193, height: 110,}}/>
        </TouchableHighlight>
      </View>
    );
  }
}