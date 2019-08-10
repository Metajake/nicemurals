var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
var renderer = new THREE.WebGLRenderer({alpha:true});
let cubeSize = 1.5;
let rotationSpeed = 0.004;
var geometry = new THREE.BoxGeometry(cubeSize, cubeSize, cubeSize);
var material = new THREE.MeshBasicMaterial({color:0x5AB2ED});
var cube = new THREE.Mesh( geometry, material );

renderer.setSize( window.innerWidth, window.innerHeight);
document.querySelector('#space').appendChild(renderer.domElement);

scene.add(cube);
camera.position.z = 5;

function animate(){
  requestAnimationFrame(animate);

  cube.rotation.x += rotationSpeed;
  cube.rotation.y += rotationSpeed;

  renderer.render(scene, camera);
}

animate();
