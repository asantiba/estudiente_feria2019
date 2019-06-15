import React, {Component} from 'react';
import ModalDiente from "./Components/modal";
import {Dimensions, Platform, StyleSheet, Text, View, Image, ImageBackground, AppRegistry, Alert, Button, TouchableWithoutFeedback} from 'react-native';


class dien-test extends React.Component {
  render() {
    return (
      <View style={{ flex: 1, flexDirection: "row" , alignItems: 'center', justifyContent: 'center' }}>
        <View style={{ flex: 1, flexDirection: "column" , alignItems: 'center', justifyContent: 'center' }}>
            <View>
                <Image source={require('./images/DientesImg/iu1.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu2.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu3.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu4.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu5.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu6.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu7.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iu8.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD8.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD7.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD6.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD5.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD4.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD3.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD2.png')} style={{height: 50, width: 50}}/>
            </View>
            <View>
                <Image source={require('./images/DientesImg/iD1.png')} style={{height: 50, width: 50}}/>
            </View>
        </View>


        <View style={{ flex: 1, flexDirection: "column" , alignItems: 'center', justifyContent: 'center' }}>
        </View>
            <Image source={require('./images/Logo.jpg')} style={{height: '55%', width: '100%'}}/>
      </View>
    );
  }
}