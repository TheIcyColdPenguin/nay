#ifdef GL_ES
precision mediump float;
# endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;


void main() {
    gl_FragColor = vec4(0.22, 0.47, 0.69, 1);
}