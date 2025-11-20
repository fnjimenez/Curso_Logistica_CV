<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ACTIVIDAD_9_CEDIS.md</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="🟦-modelado-del-cedis-en-anylogic">🟦 MODELADO DEL CEDIS EN ANYLOGIC</h1>
<div align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/4c/Logo_AnyLogic.png" alt="AnyLogic Logo" width="200">
 <img src="https://github.com/fnjimenez/Curso_Logistica_CV/raw/main/CEDIS.png?raw=true" alt="CEDIS Layout" width="600"> </div>
💬 Este modelo representa tu propuesta real del CEDIS San Bartolo. Cada bloque que configures es un paso hacia la eficiencia que justificaste en la Actividad 6 (reducción del 55% en viajes, mejora del 40% en utilización). ¡Hazlo como si fuera tu proyecto profesional! 🚀
<p>💡 <strong>Tip Global:</strong> Usa colores y nombres claros en el layout para que tu simulación sea fácil de interpretar. Esto refleja el diseño conceptual que planteaste (áreas de sorting, buffer y kitting).</p>
<p>⚠️ <strong>Error Común:</strong> No olvides configurar las unidades (horas y metros) antes de avanzar. Si fallas aquí, todo el modelo será inconsistente.</p>
<hr>
<h1 id="🟦-actividad-9-–-modelado-del-cedis-automotriz-san-bartolo-en-anylogic">🟦 ACTIVIDAD 9 – MODELADO DEL CEDIS AUTOMOTRIZ SAN BARTOLO EN ANYLOGIC</h1>
<h3 id="curso-logística-y-cadena-de-valor">Curso: Logística y Cadena de Valor</h3>
<h3 id="sistemas-de-almacenamiento-y-cedis">Sistemas de Almacenamiento y CEDIS</h3>
<h3 id="versión-2025---edición--para-principiantes">Versión: 2025 - EDICIÓN  PARA PRINCIPIANTES</h3>
<hr>
<h2 id="📌-antes-de-empezar---lee-esto-primero">📌 ANTES DE EMPEZAR - LEE ESTO PRIMERO</h2>
<h3 id="¿qué-voy-a-hacer-en-esta-actividad">¿Qué voy a hacer en esta actividad?</h3>
<p>Vas a construir un <strong>modelo de simulación</strong> del CEDIS (Centro de Distribución) San Bartolo en el software AnyLogic. Este CEDIS distribuye piezas automotrices a tres plantas ensambladoras: GM Silao, GM San Luis Potosí y BMW San Luis Potosí.</p>
<h3 id="¿qué-es-un-modelo-de-simulación">¿Qué es un modelo de simulación?</h3>
<p>Es como un <strong>videojuego de tu CEDIS</strong> donde puedes ver cómo entran camiones, se descargan, los materiales circulan por el almacén y salen hacia los clientes. Te permite probar diferentes configuraciones sin construir el almacén real.</p>
<h3 id="¿qué-necesito-saber-antes">¿Qué necesito saber antes?</h3>
<p>✅ <strong>No necesitas ser experto en programación</strong><br>
✅ Este documento te guía paso a paso<br>
✅ Cada sección tiene: 🎯 Objetivo | 🧠 Explicación | 🛠️ Qué hacer | 💡 Consejos    💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.<br>
✅ Si te atoras, busca las secciones <strong>"⚠️ PROBLEMAS COMUNES"</strong></p>
<h3 id="tiempo-estimado">Tiempo estimado</h3>
<ul>
<li><strong>Primera vez:</strong> 4-6 horas</li>
<li><strong>Con experiencia:</strong> 2-3 horas</li>
</ul>
<hr>
<h2 id="datos-de-identificación">1. DATOS DE IDENTIFICACIÓN</h2>

<table>
<thead>
<tr>
<th>Campo</th>
<th>Información a completar</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Nombre del estudiante</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Matrícula</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Carrera</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Grupo</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Fecha de entrega</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Nombre del CEDIS modelado</strong></td>
<td>CEDIS AUTOMOTRIZ SAN BARTOLO</td>
</tr>
</tbody>
</table><hr>
<h2 id="contexto-y-vínculo-con-actividades-anteriores">2. CONTEXTO Y VÍNCULO CON ACTIVIDADES ANTERIORES</h2>
<h3 id="🔗-¿de-dónde-viene-este-proyecto">🔗 ¿De dónde viene este proyecto?</h3>
<p>Esta Actividad 9 <strong>completa el trabajo</strong> que hiciste en:</p>
<ul>
<li><strong>Actividad 6:</strong> Diseñaste el CEDIS San Bartolo en papel (capacidad, áreas, flujos)</li>
<li><strong>Actividad 7:</strong> Analizaste qué industrias podrían ubicarse en la región</li>
<li><strong>Actividad 8 (opcional):</strong> Usaste métodos cuantitativos para decisiones logísticas</li>
</ul>
<p>Ahora vas a <strong>dar vida a ese diseño</strong> en una simulación digital.</p>
<h3 id="🎯-¿qué-voy-a-simular">🎯 ¿Qué voy a simular?</h3>
<ol>
<li><strong>Entrada:</strong> Camiones de 3 proveedores (Lear, Condumex, Magna)</li>
<li><strong>Procesos internos:</strong> Descarga → Clasificación → Almacenamiento → Preparación</li>
<li><strong>Salida:</strong> Despacho hacia GM Silao, GM SLP y BMW SLP</li>
</ol>
<h3 id="📊-datos-clave-del-cedis-actividad-6">📊 Datos clave del CEDIS (Actividad 6)</h3>

<table>
<thead>
<tr>
<th>Parámetro</th>
<th>Valor</th>
<th>Notas</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Capacidad</strong></td>
<td>22,000 pallets</td>
<td>Capacidad máxima de almacenamiento</td>
</tr>
<tr>
<td><strong>Entrada diaria</strong></td>
<td>~7,100 pallets</td>
<td>Flujo promedio de entrada</td>
</tr>
<tr>
<td><strong>Salida diaria</strong></td>
<td>~7,700 pallets</td>
<td>Flujo promedio de salida</td>
</tr>
<tr>
<td><strong>Andenes</strong></td>
<td>24 total</td>
<td>8 recepción + 16 embarque</td>
</tr>
<tr>
<td><strong>Cross-docking</strong></td>
<td>65%</td>
<td>Materiales que pasan directo sin almacenarse</td>
</tr>
</tbody>
</table><hr>
<h2 id="objetivo-general">3. OBJETIVO GENERAL</h2>
<blockquote>
<p><strong>Construir y documentar un modelo funcional del CEDIS en AnyLogic</strong> que simule camiones entrando, procesos de descarga, clasificación, almacenamiento y despacho hacia tres clientes automotrices, con recursos, tiempos y KPIs medibles.</p>
</blockquote>
<hr>
<h2 id="objetivos-específicos">4. OBJETIVOS ESPECÍFICOS</h2>
<h1 id="objetivos-específicos-1">4. OBJETIVOS ESPECÍFICOS</h1>

<table>
<thead>
<tr>
<th>#</th>
<th>Objetivo</th>
<th>Estado</th>
<th>Prioridad</th>
<th>Observaciones</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Configurar proyecto AnyLogic con unidades correctas</td>
<td></td>
<td>🔴 ALTA</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Crear agentes (camiones) con información de carga y destino</td>
<td></td>
<td>🔴 ALTA</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Dibujar layout básico del CEDIS</td>
<td></td>
<td>🟡 MEDIA</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Construir diagrama de flujo con bloques Process Modeling</td>
<td></td>
<td>🔴 ALTA</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Gestionar recursos (andenes, montacargas)</td>
<td></td>
<td>🔴 ALTA</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Programar decisiones de ruteo</td>
<td></td>
<td>🟡 MEDIA</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Calcular indicadores (KPIs)</td>
<td></td>
<td>🟢 BAJA</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Publicar modelo en AnyLogic Cloud</td>
<td></td>
<td>🟢 BAJA</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Crear dashboard de monitoreo</td>
<td></td>
<td>🟡 MEDIA</td>
<td></td>
</tr>
</tbody>
</table><p><strong>💡 Tip:</strong> Este paso conecta con tu diseño conceptual de la Actividad 6.</p>
<hr>
<h2 id="requisitos-previos">5. REQUISITOS PREVIOS</h2>
<h3 id="📦-software-necesario">📦 Software Necesario</h3>
<ul>
<li><strong>AnyLogic</strong> instalado (versión PLE o superior)<br>
👉 Descarga gratuita: <a href="https://www.anylogic.com/downloads/">www.anylogic.com</a></li>
</ul>
<h3 id="🧠-conocimientos-previos">🧠 Conocimientos Previos</h3>
<ul>
<li>Haber completado Actividades 6 y 7</li>
<li>Haber visto el video introductorio de AnyLogic (proporcionado por el profesor)</li>
</ul>
<h3 id="📎-materiales-de-referencia">📎 Materiales de Referencia</h3>
<ul>
<li>Layout del CEDIS San Bartolo (imagen PNG/JPG proporcionada)</li>
<li>Este documento como guía principal</li>
<li>Datos de la Actividad 6 para parámetros</li>
</ul>
<h3 id="🖼️-layout-de-referencia">🖼️ Layout de Referencia</h3>
<p><img src="https://raw.githubusercontent.com/fnjimenez/Curso_Logistica_CV/main/layoutt.png" alt="Layout CEDIS San Bartolo"></p>
<hr>
<h2 id="¿cómo-usar-este-documento">6. ¿CÓMO USAR ESTE DOCUMENTO?</h2>
<h3 id="📖-estructura-de-cada-paso">📖 Estructura de Cada Paso</h3>
<p>Cada sección sigue este formato estándar:</p>
<pre><code>🎯 OBJETIVO → Qué vas a lograr en este paso
🧠 LÓGICA → Por qué lo haces así y cómo funciona
🛠️ CONFIGURACIÓN → Instrucciones técnicas paso a paso
💻 CÓDIGO → Qué escribir exactamente en AnyLogic
💡 CONSEJOS → Trucos y mejores prácticas
⚠️ PROBLEMAS COMUNES → Soluciones rápidas a errores frecuentes
</code></pre>
<h3 id="✅-sistema-de-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.">✅ Sistema de Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<p>Al final de cada sección encontrarás:</p>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> <strong>Completado y funciona</strong> - Todo correcto</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> <strong>Completado pero tengo dudas</strong> - Necesitas revisión</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> <strong>No pude completarlo</strong> - Busca ayuda en problemas comunes</li>
</ul>
<h3 id="🎯-flujo-recomendado">🎯 Flujo Recomendado</h3>
<ol>
<li><strong>Lee completamente</strong> cada paso antes de ejecutar</li>
<li><strong>Sigue el orden numérico</strong> estrictamente</li>
<li><strong>Ejecuta y verifica</strong> después de cada paso importante</li>
<li><strong>Documenta problemas</strong> para referencia futura</li>
</ol>
<hr>
<h1 id="parte-1-configuración-inicial">PARTE 1: CONFIGURACIÓN INICIAL</h1>
<hr>
<h2 id="paso-1-crear-el-proyecto-y-configurar-unidades">1. PASO 1 CREAR EL PROYECTO Y CONFIGURAR UNIDADES</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Crear un proyecto nuevo en AnyLogic con las unidades correctas (horas y metros) para el modelo del CEDIS.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Trabajaremos en un solo agente llamado <code>Main</code> que contendrá todos los elementos:</p>
<ul>
<li>El dibujo del layout del CEDIS</li>
<li>El diagrama de flujo completo de camiones</li>
<li>Los recursos compartidos (andenes, montacargas)</li>
<li>Los indicadores de desempeño (KPIs)</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-1.1-crear-el-proyecto"><strong>Paso 1.1: Crear el Proyecto</strong></h4>
<ol>
<li>Abrir AnyLogic desde el escritorio</li>
<li>Menú <strong>File → New Model…</strong></li>
<li>En el cuadro de diálogo:
<ul>
<li><strong>Model name:</strong> <code>CEDIS_SanBartolo_TuApellido</code> (ej: <code>CEDIS_SanBartolo_Garcia</code>)</li>
<li><strong>Location:</strong> Seleccionar carpeta de tu preferencia</li>
</ul>
</li>
<li>Click en <strong>Finish</strong></li>
</ol>
<h4 id="paso-1.2-configurar-unidades-de-tiempo-y-espacio"><strong>Paso 1.2: Configurar Unidades de Tiempo y Espacio</strong></h4>
<ol>
<li>En el panel izquierdo <strong>Projects</strong>, hacer click en el <strong>nombre del modelo</strong> (no en Main)</li>
<li>En la parte inferior, buscar la pestaña <strong>Properties</strong></li>
<li>Expandir la sección <strong>Environment</strong></li>
<li>Configurar valores:
<ul>
<li><strong>Time units:</strong> seleccionar <code>hour</code> (hora)</li>
<li><strong>Length units:</strong> seleccionar <code>meter</code> (metro)</li>
</ul>
</li>
</ol>
<h4 id="paso-1.3-verificar-que-main-está-activo"><strong>Paso 1.3: Verificar que Main está Activo</strong></h4>
<ol>
<li>En panel izquierdo, hacer doble click en <strong>Main</strong></li>
<li>Debe abrirse una ventana blanca de trabajo (canvas)</li>
<li>Verificar que en la parte superior dice: <strong>Main (Agent Type)</strong></li>
</ol>
<h3 id="⚠️-problemas-comunes-y-soluciones">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No encuentro "Environment"</strong></td>
<td>No aparece la sección en Properties</td>
<td>Click en el nombre del PROYECTO, no en Main</td>
</tr>
<tr>
<td><strong>No aparece Main</strong></td>
<td>El agente Main no está visible</td>
<td>Menú Projects → click derecho → New Agent Type → Nombre: Main</td>
</tr>
<tr>
<td><strong>Las unidades no se guardan</strong></td>
<td>Al cerrar se pierde la configuración</td>
<td>Cerrar y reabrir el proyecto, verificar en Properties</td>
</tr>
<tr>
<td><strong>Error al crear proyecto</strong></td>
<td>AnyLogic se cierra o da error</td>
<td>Verificar espacio en disco y permisos de la carpeta</td>
</tr>
</tbody>
</table><h3 id="💡-consejos-prácticos">💡 CONSEJOS PRÁCTICOS</h3>
<ul>
<li><strong>Nombra bien el proyecto</strong> desde el inicio para evitar confusiones</li>
<li><strong>Las unidades son críticas</strong> - horas para tiempos, metros para distancias</li>
<li><strong>Guarda frecuentemente</strong> con Ctrl+S durante el proceso</li>
<li><strong>Mantén Main abierto</strong> - es tu área de trabajo principal</li>
</ul>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Proyecto creado con nombre personalizado correcto</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Unidades configuradas en horas y metros en Environment</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Main está abierto y visible en el canvas</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Puedo ver la ventana de Properties en la parte inferior</li>
</ul>
<hr>
<h2 id="paso-2-dibujar-el-layout-del-cedis">2. PASO 2 DIBUJAR EL LAYOUT DEL CEDIS</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-1">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Crear la representación visual del CEDIS usando el layout proporcionado como referencia, definiendo claramente todas las zonas operativas.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-1">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Un buen layout visual ayuda a:</p>
<ul>
<li>Entender el flujo de materiales</li>
<li>Ubicar correctamente los procesos</li>
<li>Comunicar el diseño a otras personas</li>
<li>Debuggear problemas en la simulación</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-1">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-2.1-insertar-la-imagen-de-fondo-altamente-recomendado"><strong>Paso 2.1: Insertar la Imagen de Fondo (ALTAMENTE RECOMENDADO)</strong></h4>
<ol>
<li>Descargar la imagen <code>layoutt.png</code> desde GitHub</li>
<li>En AnyLogic, con Main abierto, ir a menú <strong>Insert → Image…</strong></li>
<li>Navegar y seleccionar la imagen, click en <strong>Open</strong></li>
<li>Click en el canvas para colocarla como referencia</li>
<li>Ajustar tamaño arrastrando desde las esquinas</li>
</ol>
<p><strong>Para fijar la imagen y que no estorbe:</strong><br>
6. Click derecho sobre la imagen → <strong>Order → Send to Back</strong><br>
7. Click derecho → <strong>Lock</strong> (para que no se mueva accidentalmente)</p>
<h4 id="paso-2.2-dibujar-las-zonas-principales-con-rectángulos"><strong>Paso 2.2: Dibujar las Zonas Principales con Rectángulos</strong></h4>
<p>En la paleta izquierda, buscar <strong>Presentation → Space Markup → Rectangular Node</strong>:</p>

<table>
<thead>
<tr>
<th>Zona</th>
<th>Color Sugerido</th>
<th>Propósito</th>
</tr>
</thead>
<tbody>
<tr>
<td>Recepción Norte</td>
<td><code>#FFF2CC</code> (Amarillo claro)</td>
<td>Entrada camiones región norte</td>
</tr>
<tr>
<td>Recepción Sur</td>
<td><code>#FFF2CC</code> (Amarillo claro)</td>
<td>Entrada camiones región sur</td>
</tr>
<tr>
<td>Sorting</td>
<td><code>#D5E8D4</code> (Verde claro)</td>
<td>Clasificación de materiales</td>
</tr>
<tr>
<td>Buffer Estratégico</td>
<td><code>#F8CECC</code> (Rojo claro)</td>
<td>Almacenamiento temporal</td>
</tr>
<tr>
<td>Kitting</td>
<td><code>#DAE8FC</code> (Azul claro)</td>
<td>Valor agregado</td>
</tr>
<tr>
<td>Embarques GM Silao</td>
<td><code>#E1D5E7</code> (Morado claro)</td>
<td>Salida GM Silao</td>
</tr>
<tr>
<td>Embarques GM SLP</td>
<td><code>#E1D5E7</code> (Morado claro)</td>
<td>Salida GM San Luis</td>
</tr>
<tr>
<td>Embarques BMW SLP</td>
<td><code>#E1D5E7</code> (Morado claro)</td>
<td>Salida BMW</td>
</tr>
</tbody>
</table><p><strong>Para cada rectángulo:</strong></p>
<ol>
<li>Arrastrar <strong>Rectangular Node</strong> al canvas</li>
<li>Dibujar sobre la zona correspondiente en la imagen</li>
<li>Click derecho → <strong>Properties → Fill color</strong> → Elegir color</li>
<li><strong>Line color:</strong> Gris oscuro para mejor contorno</li>
</ol>
<h4 id="paso-2.3-agregar-etiquetas-de-texto-identificadoras"><strong>Paso 2.3: Agregar Etiquetas de Texto Identificadoras</strong></h4>
<ol>
<li>En paleta izquierda: <strong>Presentation → Text</strong></li>
<li>Arrastrar al canvas y colocar sobre cada zona</li>
<li>Configurar texto según esta tabla:</li>
</ol>

<table>
<thead>
<tr>
<th>Texto</th>
<th>Tamaño Fuente</th>
<th>Color</th>
<th>Ubicación</th>
</tr>
</thead>
<tbody>
<tr>
<td>“RECEPCIÓN NORTE”</td>
<td>16</td>
<td>Negro</td>
<td>Sobre recepción norte</td>
</tr>
<tr>
<td>“RECEPCIÓN SUR”</td>
<td>16</td>
<td>Negro</td>
<td>Sobre recepción sur</td>
</tr>
<tr>
<td>“SORTING”</td>
<td>14</td>
<td>Negro</td>
<td>Sobre área sorting</td>
</tr>
<tr>
<td>“BUFFER ESTRATÉGICO”</td>
<td>12</td>
<td>Negro</td>
<td>Sobre buffer</td>
</tr>
<tr>
<td>“KITTING”</td>
<td>14</td>
<td>Negro</td>
<td>Sobre kitting</td>
</tr>
<tr>
<td>“EMBARQUES GM SILAO”</td>
<td>12</td>
<td>Negro</td>
<td>Sobre embarques GM Silao</td>
</tr>
<tr>
<td>“EMBARQUES GM SLP”</td>
<td>12</td>
<td>Negro</td>
<td>Sobre embarques GM SLP</td>
</tr>
<tr>
<td>“EMBARQUES BMW SLP”</td>
<td>12</td>
<td>Negro</td>
<td>Sobre embarques BMW</td>
</tr>
</tbody>
</table><h3 id="⚠️-problemas-comunes-y-soluciones-1">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>La imagen tapa todo</strong></td>
<td>No se ven los rectángulos</td>
<td>Click derecho → Order → Send to Back</td>
</tr>
<tr>
<td><strong>No puedo mover la imagen</strong></td>
<td>La imagen está bloqueada</td>
<td>Click derecho → Unlock temporalmente</td>
</tr>
<tr>
<td><strong>Los rectángulos no se ven</strong></td>
<td>Sólo se ve el borde</td>
<td>Properties → Fill color → Elegir color sólido</td>
</tr>
<tr>
<td><strong>El texto se sale</strong></td>
<td>Las etiquetas no caben</td>
<td>Reducir tamaño de fuente o usar abreviaciones</td>
</tr>
</tbody>
</table><h3 id="💡-consejos-de-diseño">💡 CONSEJOS DE DISEÑO</h3>
<ul>
<li><strong>Usa colores consistentes</strong> - mismo color para funciones similares</li>
<li><strong>Mantén proporciones</strong> - no necesita ser exacto, pero sí reconocible</li>
<li><strong>Deja espacio para el flowchart</strong> - el layout va a la izquierda, flowchart a la derecha</li>
<li><strong>Grupa elementos relacionados</strong> - recepciones juntas, embarques juntos</li>
<li><strong>Usa la función Snap</strong> - ayuda a alinear elementos perfectamente</li>
</ul>
<h3 id="🎨-esquema-de-colores-recomendado">🎨 Esquema de Colores Recomendado</h3>
<pre><code>Recepción:    #FFF2CC  (Amarillo - Entrada)
Procesamiento: #D5E8D4  (Verde - Transformación)
Almacenamiento: #F8CECC  (Rojo - Buffer)
Salida:       #E1D5E7  (Morado - Embarques)
</code></pre>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-1">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Imagen de fondo insertada y bloqueada en posición</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 8 zonas dibujadas con rectángulos de colores diferenciados</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Todas las etiquetas de texto agregadas y legibles</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Colores consistentes según la función de cada zona</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Layout organizado y fácil de entender</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Espacio reservado para el diagrama de flujo</li>
</ul>
<hr>
<h1 id="parte-2-creación-de-agentes-y-fuentes">PARTE 2: CREACIÓN DE AGENTES Y FUENTES</h1>
<hr>
<h2 id="paso-3-crear-el-agente-truck">3. PASO 3 CREAR EL AGENTE <code>Truck</code></h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-2">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Definir la “ficha técnica” de los camiones que entrarán al CEDIS con todos sus atributos necesarios.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-2">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Cada camión es un <strong>agente</strong> que fluye por el sistema y necesita almacenar información específica:</p>
<ul>
<li><strong>Origen:</strong> Proveedor y región de procedencia</li>
<li><strong>Carga:</strong> Cantidad de pallets que transporta</li>
<li><strong>Destino:</strong> Cliente final al que va dirigido</li>
<li><strong>Tiempos:</strong> Registro de entrada y salida para métricas</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-2">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-3.1-crear-el-agente-truck"><strong>Paso 3.1: Crear el Agente Truck</strong></h4>
<ol>
<li>En panel <strong>Projects</strong>, click derecho en <strong>Agent Types</strong></li>
<li>Seleccionar <strong>New Agent Type…</strong></li>
<li>En el diálogo:
<ul>
<li><strong>Name:</strong> <code>Truck</code></li>
<li><strong>Default population:</strong> Dejar en blanco</li>
</ul>
</li>
<li>Click en <strong>Finish</strong></li>
</ol>
<h4 id="paso-3.2-agregar-atributos-variables-al-agente"><strong>Paso 3.2: Agregar Atributos (Variables) al Agente</strong></h4>

<table>
<thead>
<tr>
<th>Variable</th>
<th>Tipo</th>
<th>Valor Inicial</th>
<th>Descripción</th>
<th>Uso en el Modelo</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>proveedor</code></td>
<td>String</td>
<td><code>""</code></td>
<td>Nombre del proveedor</td>
<td>Decisiones de ruteo y estadísticas</td>
</tr>
<tr>
<td><code>region</code></td>
<td>String</td>
<td><code>""</code></td>
<td>Norte o Sur</td>
<td>Determinar recepción destino</td>
</tr>
<tr>
<td><code>destinoOEM</code></td>
<td>String</td>
<td><code>""</code></td>
<td>GM_SILAO, GM_SLP, BMW_SLP</td>
<td>Asignación final de embarque</td>
</tr>
<tr>
<td><code>pallets</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Cantidad de pallets</td>
<td>Cálculo de throughput</td>
</tr>
<tr>
<td><code>tEntradaSistema</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Hora de entrada</td>
<td>Cálculo de tiempo de ciclo</td>
</tr>
<tr>
<td><code>tSalidaSistema</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Hora de salida</td>
<td>Cálculo de tiempo de ciclo</td>
</tr>
</tbody>
</table><p><strong>Procedimiento para cada variable:</strong></p>
<ol>
<li>En el canvas de <strong>Truck</strong>, paleta superior: <strong>Agent → Variable</strong></li>
<li>Arrastrar al canvas (puedes organizarlas verticalmente)</li>
<li>En <strong>Properties</strong> configurar:
<ul>
<li><strong>Name:</strong> Nombre exacto de la variable</li>
<li><strong>Type:</strong> Seleccionar tipo correcto</li>
<li><strong>Initial value:</strong> Valor por defecto</li>
</ul>
</li>
</ol>
<h3 id="⚠️-problemas-comunes-y-soluciones-2">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No encuentro "Variable"</strong></td>
<td>No aparece en paleta</td>
<td>Buscar en pestaña Agent (icono de estrella)</td>
</tr>
<tr>
<td><strong>Error de tipo de dato</strong></td>
<td>No acepta el valor inicial</td>
<td>String: <code>""</code>, int: <code>0</code>, double: <code>0.0</code></td>
</tr>
<tr>
<td><strong>Variables no visibles</strong></td>
<td>No aparecen en el agente</td>
<td>Verificar que estás en canvas de Truck, no Main</td>
</tr>
<tr>
<td><strong>Error de nombre</strong></td>
<td>Caracteres inválidos</td>
<td>Usar solo letras, números, sin espacios</td>
</tr>
</tbody>
</table><h3 id="💡-consejos-de-buenas-prácticas">💡 CONSEJOS DE BUENAS PRÁCTICAS</h3>
<ul>
<li><strong>Nombres descriptivos:</strong> Usar <code>tEntradaSistema</code> no <code>tiempo1</code></li>
<li><strong>Organización visual:</strong> Agrupar variables relacionadas</li>
<li><strong>Comentarios:</strong> Agregar notas si es necesario</li>
<li><strong>Tipos correctos:</strong> String para texto, int para enteros, double para decimales</li>
</ul>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-2">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Agente Truck creado en Agent Types</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 6 variables agregadas con nombres exactos</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Todos los tipos de datos configurados correctamente</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Valores iniciales apropiados para cada tipo</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Variables organizadas y visibles en el canvas</li>
</ul>
<hr>
<h2 id="paso-4-crear-las-fuentes-de-camiones">4. PASO 4 CREAR LAS FUENTES DE CAMIONES</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-3">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Configurar la generación automática de camiones desde los tres proveedores principales con sus características específicas.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-3">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Cada proveedor tiene patrones únicos:</p>
<ul>
<li><strong>Frecuencias diferentes</strong> de llegada</li>
<li><strong>Regiones específicas</strong> de origen</li>
<li><strong>Capacidades distintas</strong> de carga</li>
<li><strong>Horarios preferentes</strong> de entrega</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-3">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-4.1-preparar-el-ambiente-de-trabajo"><strong>Paso 4.1: Preparar el Ambiente de Trabajo</strong></h4>
<ol>
<li>Regresar al agente <strong>Main</strong> (doble click en Projects)</li>
<li>En paleta izquierda, verificar que <strong>Process Modeling Library</strong> está visible</li>
<li>Si no está: <strong>View → Palettes → Process Modeling Library</strong></li>
</ol>
<h4 id="paso-4.2-configuración-de-sources-por-proveedor--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic."><strong>Paso 4.2: Configuración de Sources por Proveedor</strong>  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h4>

<table>
<thead>
<tr>
<th>Proveedor</th>
<th>Source Name</th>
<th>Arrival Rate</th>
<th>Pallets</th>
<th>Región</th>
<th>Horario Pico</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Lear</strong></td>
<td><code>SRC_LEAR_NORTE</code></td>
<td><code>uniform(2, 4)</code></td>
<td>26</td>
<td>NORTE</td>
<td>Mañana</td>
</tr>
<tr>
<td><strong>Condumex</strong></td>
<td><code>SRC_CONDUMEX_SUR</code></td>
<td><code>uniform(1, 3)</code></td>
<td>24</td>
<td>SUR</td>
<td>Tarde</td>
</tr>
<tr>
<td><strong>Magna</strong></td>
<td><code>SRC_MAGNA_SUR</code></td>
<td><code>uniform(1.5, 3.5)</code></td>
<td>28</td>
<td>SUR</td>
<td>Mixto</td>
</tr>
</tbody>
</table><p><strong>Procedimiento para cada Source:</strong></p>
<p><strong>Para Lear (Norte):</strong></p>
<ol>
<li>Arrastrar <strong>Source</strong> desde Process Modeling Library</li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>SRC_LEAR_NORTE</code></li>
<li><strong>Agent type:</strong> <code>Truck</code> (debe aparecer en la lista)</li>
<li><strong>Arrival rate:</strong> <code>uniform(2, 4)</code></li>
</ul>
</li>
<li>En <strong>On exit (action)</strong> escribir:</li>
</ol>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Configurar camiones Lear - Región Norte</span>
agent<span class="token punctuation">.</span>proveedor <span class="token operator">=</span> <span class="token string">"LEAR"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>region <span class="token operator">=</span> <span class="token string">"NORTE"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>pallets <span class="token operator">=</span> <span class="token number">26</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>tEntradaSistema <span class="token operator">=</span> <span class="token function">time</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// Registrar hora de entrada</span>
</code></pre>
<p><strong>Para Condumex (Sur):</strong></p>
<ol>
<li>Arrastrar otro <strong>Source</strong></li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>SRC_CONDUMEX_SUR</code></li>
<li><strong>Agent type:</strong> <code>Truck</code></li>
<li><strong>Arrival rate:</strong> <code>uniform(1, 3)</code></li>
</ul>
</li>
<li>En <strong>On exit</strong> escribir:</li>
</ol>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Configurar camiones Condumex - Región Sur</span>
agent<span class="token punctuation">.</span>proveedor <span class="token operator">=</span> <span class="token string">"CONDUMEX"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>region <span class="token operator">=</span> <span class="token string">"SUR"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>pallets <span class="token operator">=</span> <span class="token number">24</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>tEntradaSistema <span class="token operator">=</span> <span class="token function">time</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre>
<p><strong>Para Magna (Sur):</strong></p>
<ol>
<li>Arrastrar tercer <strong>Source</strong></li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>SRC_MAGNA_SUR</code></li>
<li><strong>Agent type:</strong> <code>Truck</code></li>
<li><strong>Arrival rate:</strong> <code>uniform(1.5, 3.5)</code></li>
</ul>
</li>
<li>En <strong>On exit</strong> escribir:</li>
</ol>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Configurar camiones Magna - Región Sur</span>
agent<span class="token punctuation">.</span>proveedor <span class="token operator">=</span> <span class="token string">"MAGNA"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>region <span class="token operator">=</span> <span class="token string">"SUR"</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>pallets <span class="token operator">=</span> <span class="token number">28</span><span class="token punctuation">;</span>
agent<span class="token punctuation">.</span>tEntradaSistema <span class="token operator">=</span> <span class="token function">time</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre>
<h3 id="⚠️-problemas-comunes-y-soluciones-3">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No aparece "Truck"</strong></td>
<td>No hay opción en Agent type</td>
<td>Verificar que el agente Truck está creado</td>
</tr>
<tr>
<td><strong>Error en código On exit</strong></td>
<td>Línea roja subrayada</td>
<td>Revisar puntos y coma, comillas, nombres exactos</td>
</tr>
<tr>
<td><strong>No encuentro "On exit"</strong></td>
<td>No veo la sección</td>
<td>Scroll hacia abajo en Properties, buscar “Action”</td>
</tr>
<tr>
<td><strong>Uniform no funciona</strong></td>
<td>Error en distribución</td>
<td>Verificar sintaxis: <code>uniform(min, max)</code></td>
</tr>
</tbody>
</table><h3 id="💡-consejos-de-configuración">💡 CONSEJOS DE CONFIGURACIÓN</h3>
<ul>
<li><strong>Posicionamiento:</strong> Colocar Sources en lado izquierdo del canvas, uno bajo otro</li>
<li><strong>Nomenclatura:</strong> Usar prefijos <code>SRC_</code> para identificar fácilmente</li>
<li><strong>Tasas realistas:</strong> <code>uniform(2, 4)</code> = entre 2-4 camiones/hora</li>
<li><strong>Verificación inmediata:</strong> Ejecutar modelo para ver si generan camiones</li>
</ul>
<h3 id="📊-explicación-de-distribuciones">📊 Explicación de Distribuciones</h3>
<ul>
<li><strong><code>uniform(2, 4)</code>:</strong> Valores entre 2-4 con igual probabilidad</li>
<li><strong>Resultado:</strong> ~3 camiones/hora en promedio</li>
<li><strong>Cálculo diario:</strong> 3 cam/h × 24h × 26 pallets = ~1,872 pallets/día</li>
</ul>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-3">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 3 Sources creados con nombres descriptivos</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Cada Source configurado con Agent type: Truck</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Arrival rates específicos para cada proveedor</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Código On exit correcto en cada Source</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> No hay errores (líneas rojas) en el código</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Sources posicionados ordenadamente en canvas</li>
</ul>
<hr>
<h1 id="parte-3-flujo-de-entrada-y-andenes">PARTE 3: FLUJO DE ENTRADA Y ANDENES</h1>
<hr>
<h2 id="paso-5-entrada-al-cedis-y-gestión-de-andenes">5. PASO 5 ENTRADA AL CEDIS Y GESTIÓN DE ANDENES</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-4">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Implementar el sistema de recepción donde camiones esperan, ocupan andenes, descargan y liberan recursos.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-4">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Los andenes son recursos limitados que deben gestionarse eficientemente:</p>
<ul>
<li><strong>Cola de espera</strong> cuando no hay andenes disponibles</li>
<li><strong>Seize (tomar)</strong> andén cuando se libera uno</li>
<li><strong>Delay (proceso)</strong> de descarga con tiempo variable</li>
<li><strong>Release (liberar)</strong> andén para siguiente camión</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-4">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-5.1-crear-resourcepool-de-andenes"><strong>Paso 5.1: Crear ResourcePool de Andenes</strong></h4>
<ol>
<li>En agente <strong>Main</strong>, paleta: <strong>Agent → Resource Pool</strong></li>
<li>Arrastrar al canvas (colocar en área superior derecha)</li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>docks</code></li>
<li><strong>Type:</strong> <code>Resource Units</code></li>
<li><strong>Capacity:</strong> <code>24</code></li>
<li><strong>Show name:</strong> Activado</li>
</ul>
</li>
</ol>
<h4 id="paso-5.2-construir-flowchart-de-entrada"><strong>Paso 5.2: Construir Flowchart de Entrada</strong></h4>
<p><strong>Bloque 1: Enter (Punto de Entrada Consolidado)</strong></p>
<ol>
<li>Arrastrar <strong>Enter</strong> desde Process Modeling Library</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>ENTER_CEDIS</code></li>
</ul>
</li>
<li><strong>Conectar los 3 Sources al Enter:</strong>
<ul>
<li>Click en punto naranja de cada Source</li>
<li>Arrastrar línea hasta el Enter</li>
<li>Repetir para los 3 Sources</li>
</ul>
</li>
</ol>
<p><strong>Bloque 2: Queue (Cola de Espera)</strong></p>
<ol>
<li>Arrastrar <strong>Queue</strong> a la derecha del Enter</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>Q_ANDEN</code></li>
<li><strong>Capacity:</strong> <code>unlimited</code></li>
<li><strong>Show name:</strong> Activado</li>
</ul>
</li>
</ol>
<p><strong>Bloque 3: Seize (Tomar Andén)</strong></p>
<ol>
<li>Arrastrar <strong>Seize</strong> a la derecha de Queue</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>SEIZE_ANDEN</code></li>
<li><strong>Resource sets:</strong> Click <strong>Add</strong>
<ul>
<li><strong>Resource:</strong> <code>docks</code></li>
<li><strong>Quantity:</strong> <code>1</code></li>
</ul>
</li>
</ul>
</li>
</ol>
<p><strong>Bloque 4: Delay (Proceso de Descarga)</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> a la derecha de Seize</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>UNLOAD</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.3, 0.6, 1.0)</code></li>
</ul>
</li>
</ol>
<p><strong>Bloque 5: Release (Liberar Andén)</strong></p>
<ol>
<li>Arrastrar <strong>Release</strong> a la derecha de Delay</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>RELEASE_ANDEN</code></li>
<li><strong>Resource sets:</strong> Click <strong>Add</strong> → <code>docks</code></li>
</ul>
</li>
</ol>
<h4 id="paso-5.3-conectar-todo-el-flowchart"><strong>Paso 5.3: Conectar Todo el Flowchart</strong></h4>
<pre><code>SRC_LEAR_NORTE ──┐
SRC_CONDUMEX_SUR ┼──&gt; ENTER_CEDIS → Q_ANDEN → SEIZE_ANDEN → UNLOAD → RELEASE_ANDEN
SRC_MAGNA_SUR ───┘
</code></pre>
<p><strong>Conexiones específicas:</strong></p>
<ul>
<li>Cada Source → Enter (desde punto naranja)</li>
<li>Enter → Queue</li>
<li>Queue → Seize</li>
<li>Seize → Delay</li>
<li>Delay → Release</li>
</ul>
<h3 id="⚠️-problemas-comunes-y-soluciones-4">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No puedo conectar</strong></td>
<td>Línea no se crea</td>
<td>Arrastrar desde punto naranja, no del bloque</td>
</tr>
<tr>
<td><strong>Seize no encuentra docks</strong></td>
<td>Error “cannot resolve”</td>
<td>Verificar que ResourcePool está en Main</td>
</tr>
<tr>
<td><strong>Conexión incorrecta</strong></td>
<td>Línea roja punteada</td>
<td>Rehacer conexión, verificar dirección</td>
</tr>
<tr>
<td><strong>Capacity agotada</strong></td>
<td>Cola infinita</td>
<td>Revisar Release está conectado</td>
</tr>
</tbody>
</table><h3 id="💡-consejos-de-flowchart">💡 CONSEJOS DE FLOWCHART</h3>
<ul>
<li><strong>Alinear horizontalmente</strong> para mejor visualización</li>
<li><strong>Espaciar uniformemente</strong> entre bloques</li>
<li><strong>Usar nombres descriptivos</strong> en todos los bloques</li>
<li><strong>Agrupar lógicamente</strong> procesos relacionados</li>
<li><strong>Dejar espacio</strong> para expansiones futuras</li>
</ul>
<h3 id="⏱️-tiempos-de-proceso-explicados">⏱️ Tiempos de Proceso Explicados</h3>
<ul>
<li><strong><code>triangular(0.3, 0.6, 1.0)</code>:</strong>
<ul>
<li>Mínimo: 0.3 horas (18 minutos)</li>
<li>Más probable: 0.6 horas (36 minutos)</li>
<li>Máximo: 1.0 hora (60 minutos)</li>
</ul>
</li>
<li><strong>Justificación:</strong> Depende de tipo de carga, personal disponible, etc.</li>
</ul>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-4">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> ResourcePool <code>docks</code> creado con capacidad 24</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Enter conecta los 3 Sources correctamente</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Queue con capacidad unlimited</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Seize configurado con resource <code>docks</code>, quantity 1</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Delay con distribución triangular de tiempos</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Release configurado con resource <code>docks</code></li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Todas las conexiones en secuencia correcta</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> No hay líneas rojas de error</li>
</ul>
<hr>
<h2 id="paso-6-ruteo-hacia-recepción-norte-o-sur">6. PASO 6 RUTEO HACIA RECEPCIÓN NORTE O SUR</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-5">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Implementar la decisión que dirige cada camión a la zona de recepción correcta según su región de origen.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-5">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>La separación por regiones permite:</p>
<ul>
<li><strong>Optimizar flujos</strong> internos</li>
<li><strong>Balancear cargas</strong> de trabajo</li>
<li><strong>Manejar características</strong> específicas por región</li>
<li><strong>Preparar para procesos</strong> diferenciados</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-5">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-6.1-crear-bloque-de-decisión"><strong>Paso 6.1: Crear Bloque de Decisión</strong></h4>
<ol>
<li>Arrastrar <strong>SelectOutput</strong> desde Process Modeling Library</li>
<li>Colocar a la derecha de <code>RELEASE_ANDEN</code></li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>ROUTE_RECEPCION</code></li>
<li><strong>Type:</strong> <code>Condition</code></li>
<li><strong>Condition:</strong> <code>By code</code></li>
<li><strong>Outputs:</strong> <code>2</code></li>
</ul>
</li>
</ol>
<h4 id="paso-6.2-programar-la-lógica-de-decisión--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia."><strong>Paso 6.2: Programar la Lógica de Decisión</strong>  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h4>
<h3 id="paso-6.2-configurar-tiempos-de-recepción"><strong>Paso 6.2: Configurar Tiempos de Recepción</strong></h3>
<p><strong>Agregar estos delays después del SelectOutput ROUTE_RECEPCION:</strong></p>

<table>
<thead>
<tr>
<th>Bloque</th>
<th>Nombre</th>
<th>Delay Time</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Delay</strong></td>
<td><code>DELAY_RECEP_NORTE</code></td>
<td><code>triangular(0.15, 0.25, 0.40)</code></td>
<td>Procesamiento recepción norte</td>
</tr>
<tr>
<td><strong>Delay</strong></td>
<td><code>DELAY_RECEP_SUR</code></td>
<td><code>triangular(0.15, 0.25, 0.40)</code></td>
<td>Procesamiento recepción sur</td>
</tr>
<tr>
<td><strong>Delay</strong></td>
<td><code>SORTING_PROCESS</code></td>
<td><code>triangular(0.2, 0.4, 0.8)</code></td>
<td>Clasificación central</td>
</tr>
</tbody>
</table><p><strong>Conexiones:</strong></p>
<pre><code>RELEASE_ANDEN → ROUTE_RECEPCION ─┬─(0)─&gt; DELAY_RECEP_NORTE ─┐
                                 │                           ├─&gt; SORTING_PROCESS
                                 └─(1)─&gt; DELAY_RECEP_SUR ───┘
</code></pre>
<p>En el campo de código del SelectOutput:</p>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Decidir ruta según región del camión</span>
<span class="token keyword">if</span> <span class="token punctuation">(</span>agent<span class="token punctuation">.</span>region<span class="token punctuation">.</span><span class="token function">equals</span><span class="token punctuation">(</span><span class="token string">"NORTE"</span><span class="token punctuation">)</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span class="token punctuation">;</span>  <span class="token comment">// Rama 0: Recepción Norte</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token number">1</span><span class="token punctuation">;</span>  <span class="token comment">// Rama 1: Recepción Sur</span>
<span class="token punctuation">}</span>
</code></pre>
<h4 id="paso-6.3-crear-delays-de-procesamiento-por-recepción"><strong>Paso 6.3: Crear Delays de Procesamiento por Recepción</strong></h4>
<p><strong>Para Recepción Norte:</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> arriba a la derecha del SelectOutput</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>DELAY_RECEP_NORTE</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.15, 0.25, 0.40)</code></li>
</ul>
</li>
</ol>
<p><strong>Para Recepción Sur:</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> abajo a la derecha del SelectOutput</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>DELAY_RECEP_SUR</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.15, 0.25, 0.40)</code></li>
</ul>
</li>
</ol>
<p><strong>Proceso de Sorting (Común):</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> al centro-derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>SORTING_PROCESS</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.2, 0.4, 0.8)</code></li>
</ul>
</li>
</ol>
<h4 id="paso-6.4-conectar-las-rutas"><strong>Paso 6.4: Conectar las Rutas</strong></h4>
<pre><code>RELEASE_ANDEN → ROUTE_RECEPCION ─┬─(0)─&gt; DELAY_RECEP_NORTE ─┐
                                 │                           ├─&gt; SORTING_PROCESS
                                 └─(1)─&gt; DELAY_RECEP_SUR ───┘
</code></pre>
<p><strong>Conexiones específicas:</strong></p>
<ul>
<li><code>RELEASE_ANDEN</code> → <code>ROUTE_RECEPCION</code></li>
<li>Rama 0 (superior) → <code>DELAY_RECEP_NORTE</code></li>
<li>Rama 1 (inferior) → <code>DELAY_RECEP_SUR</code></li>
<li>Ambos delays → <code>SORTING_PROCESS</code></li>
</ul>
<h3 id="⚠️-problemas-comunes-y-soluciones-5">⚠️ PROBLEMAS COMUNES Y SOLUCIONES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Síntoma</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Error "equals"</strong></td>
<td>No reconoce el método</td>
<td>Usar <code>agent.region.equals("NORTE")</code> no <code>==</code></td>
</tr>
<tr>
<td><strong>Solo 1 salida</strong></td>
<td>No veo segunda rama</td>
<td>Properties → Outputs: cambiar a <code>2</code></td>
</tr>
<tr>
<td><strong>Rama incorrecta</strong></td>
<td>Camiones van a zona equivocada</td>
<td>Verificar return 0 y return 1</td>
</tr>
<tr>
<td><strong>No se conectan</strong></td>
<td>Líneas no permitidas</td>
<td>AnyLogic permite múltiples entradas a un bloque</td>
</tr>
</tbody>
</table><h3 id="💡-consejos-de-ruteo">💡 CONSEJOS DE RUTEO</h3>
<ul>
<li><strong>Testear decisiones:</strong> Ejecutar y verificar que camiones van a zonas correctas</li>
<li><strong>Balance visual:</strong> Organizar ramas simétricamente</li>
<li><strong>Tiempos realistas:</strong> Recepción más rápida que descarga</li>
<li><strong>Preparar para expansión:</strong> Dejar espacio para más zonas si es necesario</li>
</ul>
<h3 id="⏱️-tiempos-de-recepción">⏱️ Tiempos de Recepción</h3>
<ul>
<li><strong>Recepción:</strong> <code>triangular(0.15, 0.25, 0.40)</code> = 9-24 minutos</li>
<li><strong>Sorting:</strong> <code>triangular(0.2, 0.4, 0.8)</code> = 12-48 minutos</li>
<li><strong>Diferenciación:</strong> Tiempos similares entre Norte/Sur para simplicidad</li>
</ul>
<h3 id="✅-checklist-de-verificación--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-5">✅ Checklist de Verificación  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> SelectOutput configurado con 2 salidas</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Código de decisión funciona sin errores</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 2 delays de recepción creados (Norte/Sur)</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Delay de sorting común creado</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Conexiones correctas desde SelectOutput</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Ambas ramas conectadas a Sorting</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Tiempos configurados apropiadamente</li>
</ul>
<hr>
<h1 id="🟦-actividad-9-–-modelado-del-cedis-automotriz-san-bartolo-en-anylogic-1">🟦 ACTIVIDAD 9 – MODELADO DEL CEDIS AUTOMOTRIZ SAN BARTOLO EN ANYLOGIC</h1>
<h2 id="paso-7-decisión-cross-docking-o-buffer-estratégico">7. PASO 7 DECISIÓN: CROSS-DOCKING O BUFFER ESTRATÉGICO</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-6">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Implementar la lógica que determina si los materiales pasan directo a embarque (cross-docking) o requieren almacenamiento temporal (buffer).</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-6">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Según datos reales de CEDIS automotrices:</p>
<ul>
<li><strong>65% Cross-docking:</strong> Máxima eficiencia, costo mínimo</li>
<li><strong>30% Buffer:</strong> Flexibilidad operativa, manejo de picos</li>
<li><strong>5% Kitting:</strong> Valor agregado, servicios especiales</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-6">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-7.1-crear-punto-de-decisión-de-flujo"><strong>Paso 7.1: Crear Punto de Decisión de Flujo</strong></h4>
<ol>
<li>Arrastrar <strong>SelectOutput</strong> a la derecha de <code>SORTING_PROCESS</code></li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>FLOW_DECISION</code></li>
<li><strong>Type:</strong> <code>Condition</code></li>
<li><strong>Condition:</strong> <code>By code</code></li>
<li><strong>Outputs:</strong> <code>3</code> (Cambiar de 2 a 3)</li>
</ul>
</li>
</ol>
<h4 id="paso-7.2-programar-distribución-probabilística"><strong>Paso 7.2: Programar Distribución Probabilística</strong></h4>
<p>En el campo de código:</p>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Decidir ruta según porcentajes predefinidos</span>
<span class="token keyword">double</span> randomValue <span class="token operator">=</span> <span class="token function">uniform</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">if</span> <span class="token punctuation">(</span>randomValue <span class="token operator">&lt;</span> <span class="token number">0.65</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span class="token punctuation">;</span>  <span class="token comment">// 65% - Cross-docking directo</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token keyword">if</span> <span class="token punctuation">(</span>randomValue <span class="token operator">&lt;</span> <span class="token number">0.95</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token number">1</span><span class="token punctuation">;</span>  <span class="token comment">// 30% - Buffer estratégico (0.65 + 0.30 = 0.95)</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token number">2</span><span class="token punctuation">;</span>  <span class="token comment">// 5% - Kitting/Valor agregado</span>
<span class="token punctuation">}</span>
</code></pre>
<h4 id="paso-7.3-crear-procesos-para-cada-ruta"><strong>Paso 7.3: Crear Procesos para Cada Ruta</strong></h4>
<p><strong>Ruta 1: Buffer Estratégico</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> en posición media-derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>BUFFER_TIME</code></li>
<li><strong>Delay time:</strong> <code>triangular(1, 3, 6)</code></li>
</ul>
</li>
</ol>
<p><strong>Ruta 2: Kitting/Valor Agregado</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> en posición inferior-derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>KITTING_PROCESS</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.15, 0.30, 0.50)</code></li>
</ul>
</li>
</ol>
<p><strong>Ruta 0: Cross-docking</strong> va directo al siguiente paso</p>
<h4 id="paso-7.4-conectar-las-rutas"><strong>Paso 7.4: Conectar las Rutas</strong></h4>
<pre><code>SORTING_PROCESS → FLOW_DECISION ─┬─(0)─&gt; [Cross-docking] ─┐
                                 ├─(1)─&gt; BUFFER_TIME ────┤
                                 └─(2)─&gt; KITTING_PROCESS ─┘
</code></pre>
<h3 id="⚠️-problemas-comunes">⚠️ PROBLEMAS COMUNES</h3>

<table>
<thead>
<tr>
<th>Problema</th>
<th>Solución</th>
</tr>
</thead>
<tbody>
<tr>
<td>Porcentajes incorrectos</td>
<td>Verificar: &lt;0.65=65%, 0.65-0.95=30%, &gt;0.95=5%</td>
</tr>
<tr>
<td>Solo 2 salidas</td>
<td>Properties → Outputs: cambiar a <code>3</code></td>
</tr>
<tr>
<td>Error uniform</td>
<td>Usar <code>uniform(0, 1)</code> no <code>random()</code></td>
</tr>
</tbody>
</table><h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> SelectOutput configurado con 3 salidas</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Código de distribución probabilística correcto</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Delay para Buffer creado con tiempos apropiados</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Delay para Kitting creado con tiempos apropiados</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Porcentajes suman 100%</li>
</ul>
<h2 id="paso-8-asignación-de-destino-oem">8. PASO 8 ASIGNACIÓN DE DESTINO OEM**</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-7">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Determinar a qué ensambladora final se dirige cada material.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-7">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Distribución basada en volumen:</p>
<ul>
<li><strong>GM Silao (55%):</strong> Mayor volumen</li>
<li><strong>GM SLP (33%):</strong> Volumen medio</li>
<li><strong>BMW SLP (12%):</strong> Volumen menor, alto valor</li>
</ul>
<h3 id="🛠️-configuración--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.">🛠️ Configuración  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-8.1-crear-decisión-de-destino"><strong>Paso 8.1: Crear Decisión de Destino</strong></h4>
<ol>
<li>Arrastrar <strong>SelectOutput</strong></li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>DESTINO_OEM</code></li>
<li><strong>Type:</strong> <code>Condition</code></li>
<li><strong>Condition:</strong> <code>By code</code></li>
<li><strong>Outputs:</strong> <code>3</code></li>
</ul>
</li>
</ol>
<h4 id="paso-8.2-programar-asignación"><strong>Paso 8.2: Programar Asignación</strong></h4>
<pre class=" language-java"><code class="prism  language-java"><span class="token keyword">double</span> r <span class="token operator">=</span> <span class="token function">uniform</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">if</span> <span class="token punctuation">(</span>r <span class="token operator">&lt;</span> <span class="token number">0.55</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"GM_SILAO"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token keyword">if</span> <span class="token punctuation">(</span>r <span class="token operator">&lt;</span> <span class="token number">0.88</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"GM_SLP"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">1</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"BMW_SLP"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">2</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
<h4 id="paso-8.3-conectar-flujos-anteriores"><strong>Paso 8.3: Conectar Flujos Anteriores</strong></h4>
<ul>
<li>Rama 0 de <code>FLOW_DECISION</code> → <code>DESTINO_OEM</code></li>
<li><code>BUFFER_TIME</code> → <code>DESTINO_OEM</code></li>
<li><code>KITTING_PROCESS</code> → <code>DESTINO_OEM</code></li>
</ul>
<h4 id="paso-8.4-preparación-por-cliente"><strong>Paso 8.4: Preparación por Cliente</strong></h4>

<table>
<thead>
<tr>
<th>Cliente</th>
<th>Bloque</th>
<th>Nombre</th>
<th>Delay Time</th>
</tr>
</thead>
<tbody>
<tr>
<td>GM Silao</td>
<td>Delay</td>
<td><code>PREPARE_GM_SILAO</code></td>
<td><code>triangular(0.25, 0.40, 0.60)</code></td>
</tr>
<tr>
<td>GM SLP</td>
<td>Delay</td>
<td><code>PREPARE_GM_SLP</code></td>
<td><code>triangular(0.25, 0.40, 0.60)</code></td>
</tr>
<tr>
<td>BMW SLP</td>
<td>Delay</td>
<td><code>PREPARE_BMW_SLP</code></td>
<td><code>triangular(0.30, 0.45, 0.70)</code></td>
</tr>
</tbody>
</table><p><strong>Conexiones:</strong></p>
<pre><code>DESTINO_OEM ─┬─(0)─&gt; PREPARE_GM_SILAO
             ├─(1)─&gt; PREPARE_GM_SLP
             └─(2)─&gt; PREPARE_BMW_SLP
</code></pre>
<hr>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-8">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Determinar a qué ensambladora final se dirige cada material y prepararlo para embarque.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-8">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Distribución basada en volumen de producción:</p>
<ul>
<li><strong>GM Silao (55%):</strong> Planta más grande, mayor volumen</li>
<li><strong>GM SLP (33%):</strong> Planta mediana, volumen significativo</li>
<li><strong>BMW SLP (12%):</strong> Planta premium, volumen menor pero alto valor</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-7">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-8.1-crear-punto-de-decisión-de-destino"><strong>Paso 8.1: Crear Punto de Decisión de Destino</strong></h4>
<ol>
<li>Arrastrar <strong>SelectOutput</strong> a la derecha (posición central)</li>
<li>Configurar Properties:
<ul>
<li><strong>Name:</strong> <code>DESTINO_OEM</code></li>
<li><strong>Type:</strong> <code>Condition</code></li>
<li><strong>Condition:</strong> <code>By code</code></li>
<li><strong>Outputs:</strong> <code>3</code></li>
</ul>
</li>
</ol>
<h4 id="paso-8.2-programar-asignación-de-destino"><strong>Paso 8.2: Programar Asignación de Destino</strong></h4>
<p>En el campo de código:</p>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Asignar destino final según porcentajes OEM</span>
<span class="token keyword">double</span> r <span class="token operator">=</span> <span class="token function">uniform</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">if</span> <span class="token punctuation">(</span>r <span class="token operator">&lt;</span> <span class="token number">0.55</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"GM_SILAO"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span class="token punctuation">;</span>  <span class="token comment">// 55% - GM Silao</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token keyword">if</span> <span class="token punctuation">(</span>r <span class="token operator">&lt;</span> <span class="token number">0.88</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"GM_SLP"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">1</span><span class="token punctuation">;</span>  <span class="token comment">// 33% - GM SLP (0.55 + 0.33 = 0.88)</span>
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{</span>
    agent<span class="token punctuation">.</span>destinoOEM <span class="token operator">=</span> <span class="token string">"BMW_SLP"</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">2</span><span class="token punctuation">;</span>  <span class="token comment">// 12% - BMW SLP</span>
<span class="token punctuation">}</span>
</code></pre>
<h4 id="paso-8.3-conectar-todos-los-flujos-anteriores"><strong>Paso 8.3: Conectar Todos los Flujos Anteriores</strong></h4>
<p><strong>Conectar las 3 rutas al mismo SelectOutput:</strong></p>
<ul>
<li>Rama 0 de <code>FLOW_DECISION</code> (Cross-docking) → <code>DESTINO_OEM</code></li>
<li><code>BUFFER_TIME</code> → <code>DESTINO_OEM</code></li>
<li><code>KITTING_PROCESS</code> → <code>DESTINO_OEM</code></li>
</ul>
<h4 id="paso-8.4-crear-procesos-de-preparación-por-cliente"><strong>Paso 8.4: Crear Procesos de Preparación por Cliente</strong></h4>
<p><strong>Para GM Silao:</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> arriba a la derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>PREPARE_GM_SILAO</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.25, 0.40, 0.60)</code></li>
</ul>
</li>
</ol>
<p><strong>Para GM SLP:</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> al centro-derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>PREPARE_GM_SLP</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.25, 0.40, 0.60)</code></li>
</ul>
</li>
</ol>
<p><strong>Para BMW SLP:</strong></p>
<ol>
<li>Arrastrar <strong>Delay</strong> abajo a la derecha</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>PREPARE_BMW_SLP</code></li>
<li><strong>Delay time:</strong> <code>triangular(0.30, 0.45, 0.70)</code></li>
</ul>
</li>
</ol>
<h4 id="paso-8.5-conectar-destinos"><strong>Paso 8.5: Conectar Destinos</strong></h4>
<pre><code>DESTINO_OEM ─┬─(0)─&gt; PREPARE_GM_SILAO
             ├─(1)─&gt; PREPARE_GM_SLP
             └─(2)─&gt; PREPARE_BMW_SLP
</code></pre>
<h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-1">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> SelectOutput con 3 salidas para destinos</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Código asigna correctamente destinoOEM</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Los 3 flujos anteriores conectados al mismo SelectOutput</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 3 delays de preparación creados (uno por OEM)</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Tiempos diferenciados (BMW mayor tiempo)</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Distribución porcentual suma 100%</li>
</ul>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-9">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Definir variables globales para calcular métricas de desempeño.</p>
<h3 id="🛠️-configuración--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-1">🛠️ Configuración  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<p>En agente <strong>Main</strong>, crear estas variables:</p>

<table>
<thead>
<tr>
<th>Variable</th>
<th>Tipo</th>
<th>Valor</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>palletsProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Contador total de pallets</td>
</tr>
<tr>
<td><code>trucksProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Contador total de camiones</td>
</tr>
<tr>
<td><code>avgCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Tiempo promedio en sistema</td>
</tr>
<tr>
<td><code>totalCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Acumulador para cálculo promedio</td>
</tr>
</tbody>
</table><p><strong>Ubicación:</strong> Área superior derecha del canvas de Main</p>
<h2 id="paso-9-salida-y-registro-de-métricas">9. PASO 9 SALIDA Y REGISTRO DE MÉTRICAS**</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-10">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Completar el flujo y registrar indicadores de desempeño.</p>
<h3 id="🛠️-configuración--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-2">🛠️ Configuración  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-9.1-crear-variables-kpi-en-main"><strong>Paso 9.1: Crear Variables KPI en Main</strong></h4>

<table>
<thead>
<tr>
<th>Variable</th>
<th>Tipo</th>
<th>Valor</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>palletsProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Total pallets procesados</td>
</tr>
<tr>
<td><code>trucksProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Total camiones procesados</td>
</tr>
<tr>
<td><code>avgCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Tiempo promedio en sistema</td>
</tr>
<tr>
<td><code>totalCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Acumulador para promedio</td>
</tr>
</tbody>
</table><h4 id="paso-9.2-crear-salida"><strong>Paso 9.2: Crear Salida</strong></h4>
<ol>
<li>Arrastrar <strong>Sink</strong></li>
<li><strong>Name:</strong> <code>EXIT_CEDIS</code></li>
<li>Conectar los 3 PREPARE al Sink</li>
</ol>
<h4 id="paso-9.3-código-en-exit_cedis-on-exit"><strong>Paso 9.3: Código en EXIT_CEDIS (On exit)</strong></h4>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// Registrar hora de salida</span>
agent<span class="token punctuation">.</span>tSalidaSistema <span class="token operator">=</span> <span class="token function">time</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">// Calcular tiempo de ciclo</span>
<span class="token keyword">double</span> tCiclo <span class="token operator">=</span> agent<span class="token punctuation">.</span>tSalidaSistema <span class="token operator">-</span> agent<span class="token punctuation">.</span>tEntradaSistema<span class="token punctuation">;</span>

<span class="token comment">// Actualizar contadores</span>
palletsProcessed <span class="token operator">+=</span> agent<span class="token punctuation">.</span>pallets<span class="token punctuation">;</span>
trucksProcessed <span class="token operator">+=</span> <span class="token number">1</span><span class="token punctuation">;</span>

<span class="token comment">// Actualizar tiempo promedio</span>
totalCycleTime <span class="token operator">+=</span> tCiclo<span class="token punctuation">;</span>
avgCycleTime <span class="token operator">=</span> totalCycleTime <span class="token operator">/</span> trucksProcessed<span class="token punctuation">;</span>
</code></pre>
<hr>
<hr>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-11">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Completar el flujo con la salida del sistema y registrar todos los indicadores clave de desempeño.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-9">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>El punto de salida es crítico para:</p>
<ul>
<li><strong>Liberar recursos</strong> del sistema</li>
<li><strong>Calcular métricas</strong> de desempeño</li>
<li><strong>Generar reportes</strong> automáticos</li>
<li><strong>Validar funcionamiento</strong> del modelo</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-8">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-9.1-crear-variables-globales-para-kpis"><strong>Paso 9.1: Crear Variables Globales para KPIs</strong></h4>
<p>En agente <strong>Main</strong>, crear estas variables:</p>

<table>
<thead>
<tr>
<th>Variable</th>
<th>Tipo</th>
<th>Valor</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>palletsProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Contador total de pallets</td>
</tr>
<tr>
<td><code>trucksProcessed</code></td>
<td>int</td>
<td><code>0</code></td>
<td>Contador total de camiones</td>
</tr>
<tr>
<td><code>avgCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Tiempo promedio en sistema</td>
</tr>
<tr>
<td><code>totalCycleTime</code></td>
<td>double</td>
<td><code>0.0</code></td>
<td>Acumulador para cálculo promedio</td>
</tr>
</tbody>
</table><p><strong>Procedimiento:</strong></p>
<ol>
<li>En <strong>Main</strong>, paleta: <strong>Agent → Variable</strong></li>
<li>Crear las 4 variables en área superior del canvas</li>
<li>Configurar Name, Type y Initial Value para cada una</li>
</ol>
<h4 id="paso-9.2-crear-punto-de-salida"><strong>Paso 9.2: Crear Punto de Salida</strong></h4>
<ol>
<li>Arrastrar <strong>Sink</strong> desde Process Modeling Library</li>
<li>Colocar a la derecha de los 3 delays de preparación</li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>EXIT_CEDIS</code></li>
</ul>
</li>
</ol>
<h4 id="paso-9.3-conectar-todas-las-rutas-finales"><strong>Paso 9.3: Conectar Todas las Rutas Finales</strong></h4>
<p>Conectar los 3 delays de preparación al Sink:</p>
<ul>
<li><code>PREPARE_GM_SILAO</code> → <code>EXIT_CEDIS</code></li>
<li><code>PREPARE_GM_SLP</code> → <code>EXIT_CEDIS</code></li>
<li><code>PREPARE_BMW_SLP</code> → <code>EXIT_CEDIS</code></li>
</ul>
<h4 id="paso-9.4-programar-registro-de-métricas"><strong>Paso 9.4: Programar Registro de Métricas</strong></h4>
<p>En el bloque <code>EXIT_CEDIS</code>, sección <strong>On exit</strong>:</p>
<pre class=" language-java"><code class="prism  language-java"><span class="token comment">// ===== REGISTRO DE MÉTRICAS AL SALIR =====</span>

<span class="token comment">// 1. Registrar hora de salida del sistema</span>
agent<span class="token punctuation">.</span>tSalidaSistema <span class="token operator">=</span> <span class="token function">time</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">// 2. Calcular tiempo de ciclo individual</span>
<span class="token keyword">double</span> cicloIndividual <span class="token operator">=</span> agent<span class="token punctuation">.</span>tSalidaSistema <span class="token operator">-</span> agent<span class="token punctuation">.</span>tEntradaSistema<span class="token punctuation">;</span>

<span class="token comment">// 3. Actualizar contadores de volumen</span>
palletsProcessed <span class="token operator">+=</span> agent<span class="token punctuation">.</span>pallets<span class="token punctuation">;</span>  <span class="token comment">// Sumar pallets procesados</span>
trucksProcessed <span class="token operator">+=</span> <span class="token number">1</span><span class="token punctuation">;</span>               <span class="token comment">// Incrementar contador de camiones</span>

<span class="token comment">// 4. Calcular tiempo promedio de ciclo</span>
totalCycleTime <span class="token operator">+=</span> cicloIndividual<span class="token punctuation">;</span>  <span class="token comment">// Acumular tiempos</span>
avgCycleTime <span class="token operator">=</span> totalCycleTime <span class="token operator">/</span> trucksProcessed<span class="token punctuation">;</span>  <span class="token comment">// Calcular promedio</span>
</code></pre>
<h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-2">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 4 variables KPI creadas en Main con valores iniciales</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Sink creado como punto final del flujo</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Los 3 delays de preparación conectados al Sink</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Código On exit implementado correctamente</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> No hay errores de compilación en el código</li>
</ul>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-12">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Panel visual para monitoreo en tiempo real.</p>
<h3 id="🛠️-configuración--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-3">🛠️ Configuración  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-10.1-título-del-dashboard"><strong>Paso 10.1: Título del Dashboard</strong></h4>
<ul>
<li><strong>Text:</strong> <code>📊 DASHBOARD - CEDIS SAN BARTOLO</code></li>
<li><strong>Font:</strong> Bold, Size: 18</li>
</ul>
<h4 id="paso-10.2-métricas-dinámicas"><strong>Paso 10.2: Métricas Dinámicas</strong></h4>

<table>
<thead>
<tr>
<th>Métrica</th>
<th>Texto Dinámico</th>
<th>Color</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pallets procesados</td>
<td><code>palletsProcessed</code></td>
<td>Verde</td>
</tr>
<tr>
<td>Camiones procesados</td>
<td><code>trucksProcessed</code></td>
<td>Azul</td>
</tr>
<tr>
<td>Tiempo promedio</td>
<td><code>format("%.2f", avgCycleTime)</code></td>
<td>Naranja</td>
</tr>
<tr>
<td>Utilización andenes</td>
<td><code>format("%.1f", docks.utilization() * 100)</code></td>
<td>Rojo</td>
</tr>
</tbody>
</table><hr>
<hr>
<h1 id="parte-5-recursos-adicionales-y-optimización">PARTE 5: RECURSOS ADICIONALES Y OPTIMIZACIÓN</h1>
<hr>
<h2 id="paso-10-gestión-de-montacargas-opcional">10. PASO 10 GESTIÓN DE MONTACARGAS (OPCIONAL)</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-13">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Implementar el uso de montacargas como recurso adicional para procesos internos.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-10">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Algunos procesos requieren recursos físicos:</p>
<ul>
<li><strong>Montacargas:</strong> Para mover pallets en sorting, buffer y kitting</li>
<li><strong>Operadores:</strong> Para tareas manuales</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-9">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-10.1-crear-resourcepool-de-montacargas"><strong>Paso 10.1: Crear ResourcePool de Montacargas</strong></h4>
<ol>
<li>En <strong>Main</strong>, arrastrar <strong>Resource Pool</strong></li>
<li>Configurar:
<ul>
<li><strong>Name:</strong> <code>forklifts</code></li>
<li><strong>Capacity:</strong> <code>12</code></li>
</ul>
</li>
</ol>
<h4 id="paso-10.2-usar-montacargas-en-procesos-clave"><strong>Paso 10.2: Usar Montacargas en Procesos Clave</strong></h4>
<p><strong>En SORTING_PROCESS:</strong></p>
<ol>
<li><strong>ANTES</strong> del delay: Agregar <strong>Seize</strong>
<ul>
<li><strong>Name:</strong> <code>SEIZE_FORK_SORTING</code></li>
<li><strong>Resource:</strong> <code>forklifts</code>, <strong>Quantity:</strong> <code>2</code></li>
</ul>
</li>
<li><strong>DESPUÉS</strong> del delay: Agregar <strong>Release</strong>
<ul>
<li><strong>Name:</strong> <code>RELEASE_FORK_SORTING</code></li>
<li><strong>Resource:</strong> <code>forklifts</code></li>
</ul>
</li>
</ol>
<p><strong>Reconectar:</strong> <code>DELAY_RECEP_*</code> → <code>SEIZE_FORK_SORTING</code> → <code>SORTING_PROCESS</code> → <code>RELEASE_FORK_SORTING</code> → <code>FLOW_DECISION</code></p>
<h3 id="✅-checklist-opcional--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.">✅ Checklist (Opcional)  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> ResourcePool forklifts creado</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Seize/Release agregados en al menos un proceso</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> El modelo sigue funcionando correctamente</li>
</ul>
<hr>
<h1 id="parte-6-dashboard-y-visualización">PARTE 6: DASHBOARD Y VISUALIZACIÓN</h1>
<hr>
<h2 id="paso-11-crear-dashboard-de-monitoreo">11. PASO 11 CREAR DASHBOARD DE MONITOREO</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-14">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Crear un panel de control visual que muestre en tiempo real el estado del CEDIS y las métricas clave.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-11">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Un dashboard efectivo permite:</p>
<ul>
<li><strong>Monitoreo en tiempo real</strong> de operaciones</li>
<li><strong>Identificación rápida</strong> de problemas</li>
<li><strong>Comunicación clara</strong> de resultados</li>
<li><strong>Validación visual</strong> del modelo</li>
</ul>
<h3 id="🛠️-configuración-paso-a-paso--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-10">🛠️ Configuración Paso a Paso  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-11.1-crear-título-del-dashboard"><strong>Paso 11.1: Crear Título del Dashboard</strong></h4>
<ol>
<li>En <strong>Main</strong>, paleta: <strong>Presentation → Text</strong></li>
<li>Arrastrar a esquina superior derecha</li>
<li>Configurar:
<ul>
<li><strong>Text:</strong> <code>📊 DASHBOARD - CEDIS SAN BARTOLO</code></li>
<li><strong>Font:</strong> Bold, Size: 18</li>
<li><strong>Text color:</strong> <code>#2C3E50</code></li>
</ul>
</li>
</ol>
<h4 id="paso-11.2-crear-etiquetas-y-valores-dinámicos"><strong>Paso 11.2: Crear Etiquetas y Valores Dinámicos</strong></h4>
<p><strong>Para Pallets Procesados:</strong></p>
<ol>
<li><strong>Texto estático:</strong> <code>Pallets procesados:</code></li>
<li><strong>Texto dinámico:</strong> <code>palletsProcessed</code>
<ul>
<li><strong>Font:</strong> Bold, Size: 14, Color: Verde</li>
</ul>
</li>
</ol>
<p><strong>Para Camiones Procesados:</strong></p>
<ol>
<li><strong>Texto estático:</strong> <code>Camiones procesados:</code></li>
<li><strong>Texto dinámico:</strong> <code>trucksProcessed</code>
<ul>
<li><strong>Font:</strong> Bold, Size: 14, Color: Azul</li>
</ul>
</li>
</ol>
<p><strong>Para Tiempo Promedio:</strong></p>
<ol>
<li><strong>Texto estático:</strong> <code>Tiempo promedio (horas):</code></li>
<li><strong>Texto dinámico:</strong> <code>format("%.2f", avgCycleTime)</code>
<ul>
<li><strong>Font:</strong> Bold, Size: 14, Color: Naranja</li>
</ul>
</li>
</ol>
<p><strong>Para Utilización Andenes:</strong></p>
<ol>
<li><strong>Texto estático:</strong> <code>Utilización andenes (%):</code></li>
<li><strong>Texto dinámico:</strong> <code>format("%.1f", docks.utilization() * 100)</code>
<ul>
<li><strong>Font:</strong> Bold, Size: 14, Color: Rojo</li>
</ul>
</li>
</ol>
<h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-3">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Título del dashboard creado</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 4 etiquetas estáticas de métricas</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> 4 valores dinámicos vinculados a variables</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Formato correcto para números decimales</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Dashboard organizado y legible</li>
</ul>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-15">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Implementar montacargas como recurso adicional.</p>
<h3 id="🛠️-configuración--✅-consejo-sigue-el-orden-exacto-para-evitar-errores-en-anylogic.-4">🛠️ Configuración  ✅ <em>Consejo:</em> Sigue el orden exacto para evitar errores en AnyLogic.</h3>
<h4 id="paso-11.1-crear-resourcepool"><strong>Paso 11.1: Crear ResourcePool</strong></h4>
<ul>
<li><strong>Name:</strong> <code>forklifts</code></li>
<li><strong>Capacity:</strong> <code>12</code></li>
</ul>
<h4 id="paso-11.2-usar-en-procesos"><strong>Paso 11.2: Usar en Procesos</strong></h4>
<p>Agregar <strong>Seize/Release</strong> alrededor de <code>SORTING_PROCESS</code>:</p>
<ul>
<li><strong>Seize:</strong> <code>forklifts</code>, Quantity: <code>2</code></li>
<li><strong>Release:</strong> <code>forklifts</code></li>
</ul>
<hr>
<h1 id="parte-7-ejecución-y-publicación">PARTE 7: EJECUCIÓN Y PUBLICACIÓN</h1>
<hr>
<h2 id="paso-12-ejecución-y-validación">12. PASO 12 EJECUCIÓN Y VALIDACIÓN</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-16">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Verificar que el modelo funciona correctamente y produce resultados dentro de rangos esperados.</p>
<h3 id="🧠-lógica--📌-recuerda-justificaste-esta-lógica-en-tu-ensayo-reducción-de-viajes-eficiencia.-12">🧠 Lógica  📌 <em>Recuerda:</em> Justificaste esta lógica en tu ensayo (reducción de viajes, eficiencia).</h3>
<p>Las pruebas validan que:</p>
<ul>
<li><strong>El flujo es continuo</strong> sin bloqueos</li>
<li><strong>Las métricas son razonables</strong> según diseño</li>
<li><strong>Los recursos se utilizan</strong> eficientemente</li>
<li><strong>No hay errores</strong> de programación</li>
</ul>
<h3 id="🛠️-procedimiento-de-pruebas">🛠️ Procedimiento de Pruebas</h3>
<h4 id="paso-12.1-ejecución-inicial"><strong>Paso 12.1: Ejecución Inicial</strong></h4>
<ol>
<li>Click en botón <strong>Run</strong> (▶️)</li>
<li>Observar comportamiento por 5-10 minutos</li>
<li>Verificar flujo continuo de camiones</li>
</ol>
<h4 id="paso-12.2-validación-de-métricas"><strong>Paso 12.2: Validación de Métricas</strong></h4>
<p>Después de 24 horas simuladas:</p>

<table>
<thead>
<tr>
<th>KPI</th>
<th>Rango Esperado</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Pallets procesados</strong></td>
<td>6,000 - 8,000</td>
</tr>
<tr>
<td><strong>Camiones procesados</strong></td>
<td>200 - 300</td>
</tr>
<tr>
<td><strong>Tiempo ciclo promedio</strong></td>
<td>2.5 - 4.5 horas</td>
</tr>
<tr>
<td><strong>Utilización andenes</strong></td>
<td>65% - 85%</td>
</tr>
</tbody>
</table><h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-4">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Modelo ejecuta sin errores</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Camiones fluyen de inicio a fin</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Dashboard muestra datos reales</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Métricas en rangos esperados</li>
</ul>
<hr>
<h2 id="paso-13-publicación-en-anylogic-cloud">13. PASO 13 PUBLICACIÓN EN ANYLOGIC CLOUD</h2>
<h3 id="🎯-objetivo--💡-tip-este-paso-conecta-con-tu-diseño-conceptual-de-la-actividad-6.-17">🎯 Objetivo  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.</h3>
<p>Publicar el modelo en la nube para compartirlo.</p>
<h3 id="🛠️-procedimiento">🛠️ Procedimiento</h3>
<h4 id="paso-13.1-exportar-a-la-nube"><strong>Paso 13.1: Exportar a la Nube</strong></h4>
<ol>
<li>Menú: <strong>File → Export → To AnyLogic Cloud…</strong></li>
<li>Configurar:
<ul>
<li><strong>Model name:</strong> <code>CEDIS_SanBartolo_TuApellido_Matricula</code></li>
<li><strong>Access:</strong> <code>Public</code></li>
</ul>
</li>
<li>Click en <strong>Upload</strong></li>
</ol>
<h4 id="paso-13.2-probar-en-navegador"><strong>Paso 13.2: Probar en Navegador</strong></h4>
<ol>
<li>Copiar URL proporcionada</li>
<li>Abrir en navegador web</li>
<li>Verificar funcionalidad</li>
</ol>
<h3 id="✅-checklist--🧐-verifica-si-todo-coincide-con-los-parámetros-del-cedis-san-bartolo-22000-pallets-24-andenes.-5">✅ Checklist  🧐 <em>Verifica:</em> Si todo coincide con los parámetros del CEDIS San Bartolo (22,000 pallets, 24 andenes).</h3>
<ul>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Modelo exportado sin errores</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> URL copiada y guardada</li>
<li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled=""> Modelo accesible públicamente</li>
</ul>
<hr>
<h2 id="🎯-resumen-de-completitud">🎯 RESUMEN DE COMPLETITUD</h2>
<h3 id="✅-configuraciones-ahora-completas">✅ <strong>CONFIGURACIONES AHORA COMPLETAS:</strong></h3>
<p>| Objetivo | Estado |  💡 <em>Tip:</em> Este paso conecta con tu diseño conceptual de la Actividad 6.<br>
|----------|--------|<br>
| 1. Configurar proyecto AnyLogic | ✅ COMPLETO |<br>
| 2. Crear agentes (camiones) | ✅ COMPLETO |<br>
| 3. Dibujar layout del CEDIS | ✅ COMPLETO |<br>
| 4. Construir diagrama de flujo | ✅ COMPLETO |<br>
| 5. Gestionar recursos | ✅ COMPLETO |<br>
| 6. Programar decisiones de ruteo | ✅ COMPLETO |<br>
| 7. Calcular indicadores (KPIs) | ✅ COMPLETO |<br>
| 8. Publicar en AnyLogic Cloud | ✅ COMPLETO |<br>
| 9. Crear dashboard de monitoreo | ✅ COMPLETO |</p>
<h3 id="📊-flujo-completo-implementado">📊 <strong>FLUJO COMPLETO IMPLEMENTADO:</strong></h3>
<pre><code>SRC_LEAR ──┐
SRC_COND ──┼─&gt; ENTER → Q_ANDEN → SEIZE → UNLOAD → RELEASE → ROUTE_RECEPCION
SRC_MAGNA ─┘                                         │
                                                     ↓
                                              ┌─ RECEP_NORTE ─┐
                                              │               │
                                              └─ RECEP_SUR ───┘
                                                     │
                                                SORTING_PROCESS
                                                     │
                                               FLOW_DECISION
                                              /      |      \
                                      Cross-docking Buffer Kitting
                                            |        |        |
                                            ↓        ↓        ↓
                                         DESTINO_OEM (Convergen)
                                            /        |        \
                                    GM_SILAO     GM_SLP     BMW_SLP
                                       |            |           |
                                       ↓            ↓           ↓
                                    EXIT_CEDIS → KPIs &amp; Dashboard
</code></pre>
<p><strong>¡Listo para entregar! 🎯</strong></p>
</div>
</body>

</html>
