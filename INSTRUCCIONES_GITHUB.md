# 🚀 INSTRUCCIONES PARA SUBIR A GITHUB

## 📋 Pasos para actualizar tu repositorio

Sigue estos pasos **en orden** para subir todos los archivos a tu repositorio de GitHub.

---

## ✅ PRE-REQUISITOS

Antes de empezar, asegúrate de tener:

- [x] Git instalado en tu computadora
- [x] Cuenta de GitHub activa
- [x] Acceso al repositorio `fnjimenez/Curso_Logistica_CV`

**Verificar Git:**
```bash
git --version
```

Si no tienes Git: https://git-scm.com/downloads

---

## 🔑 PASO 1: Configurar Git (Solo la primera vez)

```bash
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email (el mismo de GitHub)
git config --global user.email "tu-email@ejemplo.com"

# Verificar configuración
git config --list
```

---

## 📥 PASO 2: Clonar o Actualizar tu Repositorio

### Si NO tienes el repositorio en tu computadora:

```bash
# Navegar a donde quieres guardar el proyecto
cd ~/Documentos  # o donde prefieras

# Clonar el repositorio
git clone https://github.com/fnjimenez/Curso_Logistica_CV.git

# Entrar al directorio
cd Curso_Logistica_CV
```

### Si YA tienes el repositorio clonado:

```bash
# Navegar al directorio
cd ruta/a/Curso_Logistica_CV

# Obtener últimos cambios
git pull origin main
```

---

## 📂 PASO 3: Copiar los Archivos Nuevos

Tienes dos opciones:

### Opción A: Descargar desde Claude (Recomendado)

1. **Descarga todos los archivos** desde los links que te proporcioné
2. **Descomprime** el ZIP (si los descargaste así)
3. **Copia TODO el contenido** al directorio de tu repositorio local

```bash
# Ejemplo en terminal (ajusta las rutas)
cp -r ~/Descargas/github_upload/* ~/Documentos/Curso_Logistica_CV/
```

### Opción B: Copiar manualmente

Copia estos archivos/directorios a tu repositorio local:

```
Curso_Logistica_CV/
├── README.md                    (REEMPLAZAR el actual)
├── LICENSE                      (NUEVO)
├── requirements.txt             (REEMPLAZAR o CREAR)
├── setup.py                     (NUEVO)
├── .gitignore                   (REEMPLAZAR o CREAR)
│
├── notebooks/
│   ├── Amazon_Logistics_v3.2.ipynb  (tu archivo actual, renombrado)
│   └── Amazon_Logistics_v4.0.ipynb  (NUEVO - próximo paso)
│
├── src/
│   ├── __init__.py              (NUEVO)
│   └── models.py                (NUEVO)
│
├── docs/
│   ├── AUDITORIA_COMPLETA.md    (NUEVO)
│   ├── GUIA_INSTALACION.md      (NUEVO)
│   ├── PROBLEMA_RED_MULTINIVEL.md (NUEVO)
│   └── correcciones_rapidas.md  (NUEVO)
│
├── examples/
│   └── ejemplo_basico.py        (NUEVO)
│
├── tests/
│   └── test_amazon_logistics.py (NUEVO)
│
└── results/
    └── .gitkeep                 (NUEVO - solo mantiene carpeta)
```

---

## 📝 PASO 4: Verificar Cambios

```bash
# Ver qué archivos cambiaron
git status

# Ver los cambios en detalle
git diff
```

Deberías ver muchos archivos en verde (nuevos) y algunos modificados.

---

## ➕ PASO 5: Agregar Archivos al Staging

```bash
# Opción 1: Agregar TODO (recomendado si revisaste los cambios)
git add .

# Opción 2: Agregar archivos específicos
git add README.md
git add requirements.txt
git add src/
git add docs/
# ... etc

# Verificar qué se agregó
git status
```

---

## 💬 PASO 6: Hacer Commit

```bash
git commit -m "feat: Agregar modelo multi-nivel y documentación completa

- Agregar modelo de 2 niveles con centros de distribución
- Incluir auditoría técnica completa
- Agregar documentación y guías
- Incluir tests unitarios
- Actualizar README con instrucciones
- Agregar ejemplos de uso

Version 4.0"
```

**Tip:** Si el commit falla, verifica que configuraste tu nombre y email (PASO 1)

---

## 🚀 PASO 7: Subir a GitHub

```bash
# Subir cambios a la rama main
git push origin main
```

**Si es tu primera vez haciendo push**, Git te pedirá autenticación:

### Autenticación con Personal Access Token (Recomendado)

1. Ve a GitHub: https://github.com/settings/tokens
2. Click en "Generate new token" → "Classic"
3. Dale un nombre: "Curso_Logistica_CV"
4. Marca los permisos: `repo` (completo)
5. Click "Generate token"
6. **COPIA EL TOKEN** (no lo volverás a ver)
7. Cuando Git pida contraseña, **pega el token** (no tu contraseña normal)

### Autenticación con GitHub CLI (Alternativa)

```bash
# Instalar GitHub CLI
# Windows: https://cli.github.com/
# Mac: brew install gh
# Linux: https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Autenticar
gh auth login

# Seguir las instrucciones
```

---

## ✅ PASO 8: Verificar en GitHub

1. Ve a: https://github.com/fnjimenez/Curso_Logistica_CV
2. Deberías ver todos los archivos nuevos
3. Verifica que el README se vea bien
4. Revisa que las carpetas `docs/`, `src/`, etc. estén ahí

---

## 🎨 PASO 9: Personalizar (Opcional)

### Actualizar el README con tu info

Edita `README.md` y cambia:

```markdown
**Francisco Jiménez**
- GitHub: [@fnjimenez](https://github.com/fnjimenez)
- Email: TU-EMAIL-REAL@ejemplo.com  # <-- CAMBIAR ESTO
```

### Agregar badges personalizados

En el README, puedes agregar badges de:
- Build status
- Coverage
- Downloads
- Etc.

Visita: https://shields.io/

---

## 🌿 PASO 10: Crear Rama de Desarrollo (Opcional pero Recomendado)

```bash
# Crear rama para desarrollo futuro
git checkout -b develop

# Subir la rama
git push origin develop

# Volver a main
git checkout main
```

Ahora puedes trabajar en `develop` y hacer merge a `main` solo cuando esté listo.

---

## 🔄 COMANDOS ÚTILES PARA EL FUTURO

### Hacer cambios posteriores

```bash
# 1. Hacer cambios en archivos
# 2. Ver qué cambió
git status

# 3. Agregar cambios
git add archivo_modificado.py

# 4. Commit
git commit -m "fix: Corregir error en visualización"

# 5. Push
git push origin main
```

### Ver historial

```bash
# Ver commits recientes
git log --oneline

# Ver cambios de un commit específico
git show abc123
```

### Deshacer cambios

```bash
# Antes de hacer commit (deshacer cambios en archivo)
git checkout -- archivo.py

# Después de commit (revertir último commit)
git revert HEAD

# Volver a un commit anterior (CUIDADO - destructivo)
git reset --hard abc123
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "Permission denied"

**Causa:** No tienes permisos para subir al repositorio.

**Solución:**
1. Verifica que eres el dueño del repositorio
2. Usa un Personal Access Token con permisos `repo`
3. O clona con SSH: `git clone git@github.com:fnjimenez/Curso_Logistica_CV.git`

### Error: "Your branch is behind"

**Causa:** Hay cambios en GitHub que no tienes localmente.

**Solución:**
```bash
git pull origin main
# Si hay conflictos, resuélvelos manualmente
git push origin main
```

### Error: "Merge conflict"

**Causa:** Dos personas editaron el mismo archivo.

**Solución:**
```bash
# 1. Git te mostrará los archivos en conflicto
git status

# 2. Abre los archivos y busca:
<<<<<<< HEAD
tu código
=======
código de GitHub
>>>>>>> origin/main

# 3. Decide qué mantener y elimina los marcadores
# 4. Guarda el archivo
# 5. Marca como resuelto
git add archivo_con_conflicto.py

# 6. Completa el merge
git commit -m "resolve: Resolver conflictos de merge"
git push origin main
```

### Error: "Repository not found"

**Causa:** URL del repositorio incorrecta o sin permisos.

**Solución:**
```bash
# Verificar remotes
git remote -v

# Si es incorrecto, cambiar
git remote set-url origin https://github.com/fnjimenez/Curso_Logistica_CV.git
```

---

## 📚 RECURSOS

- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **GitHub Learning Lab**: https://lab.github.com/
- **Markdown Guide**: https://www.markdownguide.org/

---

## ✅ CHECKLIST FINAL

Antes de considerar que terminaste:

- [ ] Todos los archivos copiados al repositorio local
- [ ] `git status` muestra los cambios correctos
- [ ] Commit realizado con mensaje descriptivo
- [ ] Push exitoso a GitHub
- [ ] Verificado en https://github.com/fnjimenez/Curso_Logistica_CV
- [ ] README se ve bien en GitHub
- [ ] Archivos en las carpetas correctas
- [ ] .gitignore funcionando (no subiste archivos temporales)
- [ ] Email y nombre personalizados en README

---

## 🎉 ¡LISTO!

Tu repositorio ahora tiene:
- ✅ Documentación completa
- ✅ Código mejorado y organizado
- ✅ Tests unitarios
- ✅ Ejemplos de uso
- ✅ Modelo multi-nivel implementado
- ✅ README profesional

**Siguiente paso:** ¡Compartir tu repo y empezar a recibir estrellas! ⭐

---

**¿Necesitas ayuda?** Abre un issue en el repositorio o envía un mensaje.

*Guía creada: Octubre 2025*
