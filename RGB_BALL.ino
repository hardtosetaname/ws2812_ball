#include <ESP8266WiFi.h>
#include <FastLED.h>  
#define LED_PIN     1 
#define NUM_LEDS    194
#define LED_TYPE    WS2812 
#define COLOR_ORDER GRB 
#define _DLY_ 50 
#define deltaHue  1
#define max_bright  128
CRGB leds[NUM_LEDS]; 
int port = 2666;
uint8_t beginHue=0;
WiFiServer server(port);
int ANALOG_PIN = A0;
const char *ssid = "RGB_BALL";  
const char *password = "2444666668888888";  //12345678
void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_AP);
    WiFi.softAP(ssid, password);
    Serial.print("IP address: ");
    Serial.println(WiFi.softAPIP());
    server.begin();
    FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
    FastLED.setBrightness(max_bright);
}
void loop() {
  char pp = 0;
    unsigned char asa[4] = {0};
  CRGB myRGBcolor(32,32,32);
 while(1)
 {
 fill_rainbow(leds, NUM_LEDS, beginHue, deltaHue); 
    FastLED.show();
    beginHue++;
  delay(_DLY_);
    WiFiClient client = server.available();
    if (client) {
        if(client.connected())
        {
            fill_solid(leds, NUM_LEDS, myRGBcolor);
            FastLED.show();
        }
         
        while(client.connected()){
            while(client.available()>0){
              client.read(asa,4);
                if (asa[0]==194){
                  if (asa[1])
                  FastLED.show();
                  else
                  client.println(analogRead(ANALOG_PIN));
                }
                else
                pp = 0;
                myRGBcolor.r=asa[1];
                myRGBcolor.g=asa[2];
                myRGBcolor.b=asa[3];
                leds[asa[0]] = myRGBcolor;
            }
          client.flush();
        }
        client.stop();
        fill_solid(leds, NUM_LEDS, CRGB::Black);
        FastLED.show();
    }
 }
}
