# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "SpeedWork",
    "author" : "Gabriel Gomides Surjus", 
    "description" : "",
    "blender" : (4, 1, 1),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "https://linktr.ee/GgomidesS", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import os
from .easybpy import *


addon_keymaps = {}
_icons = None


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


class SNA_PT_SPEEDWORK_0B345(bpy.types.Panel):
    bl_label = 'SpeedWork'
    bl_idname = 'SNA_PT_SPEEDWORK_0B345'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'SpeedWork'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.applyall_66e0f', text='Apply All', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.limpaarquivo_702d2', text='Limpa Arquivo', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.clearparent_c9bb3', text='Clear Parent', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.renomeiamalha_ae2ce', text='Renomeia Malha', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.autouv_b9591', text='AutoUV', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.autolm_113c4', text='AutoLM', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.selecionaobjetosuverrado_408f4', text='Seleciona Objetos Com UV Errado', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)
        op = layout.operator('sna.selecionaobjetoslmerrado_0c83d', text='Seleciona Objetos Com LM Errado', icon_value=load_preview_icon(r'C:\Users\ggomi\Downloads\photo_2024-06-20_15-11-38.jpg'), emboss=True, depress=False)


class SNA_OT_Limpaarquivo_702D2(bpy.types.Operator):
    bl_idname = "sna.limpaarquivo_702d2"
    bl_label = "LimpaArquivo"
    bl_description = "Remove arquivos e materiais nao usados"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        ObjetosSelecionados = selected_objects()
        for obj in ObjetosSelecionados:
            if obj.type == 'MESH':        
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.material_slot_remove_unused()
        i = int(0)   
        while i < 20:    
            bpy.ops.outliner.orphans_purge(do_recursive=True)
            i = i + 1
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Applyall_66E0F(bpy.types.Operator):
    bl_idname = "sna.applyall_66e0f"
    bl_label = "ApplyAll"
    bl_description = "Aplica Location, Rotation e Scale de todos os objetos visto na viewport"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        select_all_objects()
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Clearparent_C9Bb3(bpy.types.Operator):
    bl_idname = "sna.clearparent_c9bb3"
    bl_label = "ClearParent"
    bl_description = "Limpa o Parent de todos os objetos visto na viewport"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        select_all_objects()
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Renomeiamalha_Ae2Ce(bpy.types.Operator):
    bl_idname = "sna.renomeiamalha_ae2ce"
    bl_label = "RenomeiaMalha"
    bl_description = "Renomeia a malha com o nome do objeto"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        ObjetosSelecionados = selected_objects()
        for obj in ObjetosSelecionados:
            if obj.type == 'MESH':
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                bpy.context.view_layer.objects.active.data.name = bpy.context.view_layer.objects.active.name
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Autouv_B9591(bpy.types.Operator):
    bl_idname = "sna.autouv_b9591"
    bl_label = "AutoUV"
    bl_description = "Deleta todos os canais de UV, dos objetos selecionados, e cria um chamado 'UV' e abre automaticamente. Necessita UVpackmaster 2"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        def deletaUVs(objetos):
            for obj in objetos:
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                objetoAtivo = bpy.context.active_object
                while objetoAtivo.data.uv_layers:
                    objetoAtivo.data.uv_layers.remove(obj.data.uv_layers[0])
                #----------------------------------------------------------------------------------------------------

        def criaCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                bpy.ops.mesh.uv_texture_add()   
                bpy.context.object.data.uv_layers["UVMap"].name = nomeCanal
                #----------------------------------------------------------------------------------------------------

        def abreCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj       
                if (nomeCanal == 'UV'):
                    packUV(obj, 4, 2, 1024)
                elif(nomeCanal == 'LM'):
                    packUV(obj, 8, 4, 512)
        #----------------------------------------------------------------------------------------------------

        def packUV(objeto, margin, padding, texSize):
            if bpy.context.object.mode != 'EDIT':
                set_edit_mode(objeto)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.cube_project(cube_size=2)
            bpy.context.scene.uvp2_props.pixel_margin = margin
            bpy.context.scene.uvp2_props.pixel_padding = padding
            bpy.context.scene.uvp2_props.pixel_margin_tex_size = texSize
            bpy.ops.uv.average_islands_scale()
            bpy.ops.uvpackmaster2.uv_pack()       
            set_object_mode(objeto)
        objetosSelecionados = selected_objects()
        deletaUVs(objetosSelecionados)
        criaCanalUV(objetosSelecionados, 'UV')    
        abreCanalUV(objetosSelecionados, 'UV')
        #----------------------------------------------------------------------------------------------------
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Autolm_113C4(bpy.types.Operator):
    bl_idname = "sna.autolm_113c4"
    bl_label = "AutoLM"
    bl_description = "Cria um canal chamado 'LM' e abre automaticamente, nos objetos selecionados. Necessita UVpackmaster 2"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        def deletaUVs(objetos):
            for obj in objetos:
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                objetoAtivo = bpy.context.active_object
                while objetoAtivo.data.uv_layers:
                    objetoAtivo.data.uv_layers.remove(obj.data.uv_layers[0])
                #----------------------------------------------------------------------------------------------------

        def criaCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                bpy.ops.mesh.uv_texture_add()   
                bpy.context.object.data.uv_layers["UVMap"].name = nomeCanal
                #----------------------------------------------------------------------------------------------------

        def abreCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj       
                if (nomeCanal == 'UV'):
                    packUV(obj, 4, 2, 1024)
                elif(nomeCanal == 'LM'):
                    packUV(obj, 8, 4, 512)
        #----------------------------------------------------------------------------------------------------

        def packUV(objeto, margin, padding, texSize):
            if bpy.context.object.mode != 'EDIT':
                set_edit_mode(objeto)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.cube_project(cube_size=2)
            bpy.context.scene.uvp2_props.pixel_margin = margin
            bpy.context.scene.uvp2_props.pixel_padding = padding
            bpy.context.scene.uvp2_props.pixel_margin_tex_size = texSize
            bpy.ops.uv.average_islands_scale()
            bpy.ops.uvpackmaster2.uv_pack()       
            set_object_mode(objeto)
        objetosSelecionados = selected_objects()
        criaCanalUV(objetosSelecionados, 'LM')    
        abreCanalUV(objetosSelecionados, 'LM')
        #----------------------------------------------------------------------------------------------------
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Autouvlm_Ab75F(bpy.types.Operator):
    bl_idname = "sna.autouvlm_ab75f"
    bl_label = "AutoUVLM"
    bl_description = "Faz o 'AutoUV' e 'AutoLM' junto"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        def deletaUVs(objetos):
            for obj in objetos:
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                objetoAtivo = bpy.context.active_object
                while objetoAtivo.data.uv_layers:
                    objetoAtivo.data.uv_layers.remove(obj.data.uv_layers[0])
                #----------------------------------------------------------------------------------------------------

        def criaCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                bpy.ops.mesh.uv_texture_add()   
                bpy.context.object.data.uv_layers["UVMap"].name = nomeCanal
                #----------------------------------------------------------------------------------------------------

        def abreCanalUV(objetos, nomeCanal):
            for obj in objetos:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj       
                if (nomeCanal == 'UV'):
                    packUV(obj, 4, 2, 1024)
                elif(nomeCanal == 'LM'):
                    packUV(obj, 8, 4, 512)
        #----------------------------------------------------------------------------------------------------

        def packUV(objeto, margin, padding, texSize):
            if bpy.context.object.mode != 'EDIT':
                set_edit_mode(objeto)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.cube_project(cube_size=2)
            bpy.context.scene.uvp2_props.pixel_margin = margin
            bpy.context.scene.uvp2_props.pixel_padding = padding
            bpy.context.scene.uvp2_props.pixel_margin_tex_size = texSize
            bpy.ops.uv.average_islands_scale()
            bpy.ops.uvpackmaster2.uv_pack()       
            set_object_mode(objeto)
        objetosSelecionados = selected_objects()
        deletaUVs(objetosSelecionados)
        criaCanalUV(objetosSelecionados, 'UV')    
        abreCanalUV(objetosSelecionados, 'UV')
        criaCanalUV(objetosSelecionados, 'LM')
        abreCanalUV(objetosSelecionados, 'LM')
        #----------------------------------------------------------------------------------------------------
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Selecionaobjetosuverrado_408F4(bpy.types.Operator):
    bl_idname = "sna.selecionaobjetosuverrado_408f4"
    bl_label = "SelecionaObjetosUVErrado"
    bl_description = "Pega todos os objetos visiveis na viewport e deixa visivel apenas os objetos com o canal UV errada"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        select_all_objects()
        objetosSelecionados = selected_objects()
        for obj in objetosSelecionados:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                key = False
                if len(bpy.context.object.data.uv_layers) == 1 and bpy.context.object.data.uv_layers[0].name == 'UV':
                    key = True
                if key:
                    hide(obj)
        #----------------------------------------------------------------------------------------------------
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Selecionaobjetoslmerrado_0C83D(bpy.types.Operator):
    bl_idname = "sna.selecionaobjetoslmerrado_0c83d"
    bl_label = "SelecionaObjetosLMErrado"
    bl_description = "Pega todos os objetos visiveis na viewport e deixa visivel apenas os objetos com o canal LM errada"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        select_all_objects()
        objetosSelecionados = selected_objects()
        for obj in objetosSelecionados:        
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = obj
                key = False
                if len(bpy.context.object.data.uv_layers) == 2 and bpy.context.object.data.uv_layers[0].name == 'LM':
                    key = True
                if key:
                    hide(obj)
        #----------------------------------------------------------------------------------------------------
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_SPEEDWORK_0B345)
    bpy.utils.register_class(SNA_OT_Limpaarquivo_702D2)
    bpy.utils.register_class(SNA_OT_Applyall_66E0F)
    bpy.utils.register_class(SNA_OT_Clearparent_C9Bb3)
    bpy.utils.register_class(SNA_OT_Renomeiamalha_Ae2Ce)
    bpy.utils.register_class(SNA_OT_Autouv_B9591)
    bpy.utils.register_class(SNA_OT_Autolm_113C4)
    bpy.utils.register_class(SNA_OT_Autouvlm_Ab75F)
    bpy.utils.register_class(SNA_OT_Selecionaobjetosuverrado_408F4)
    bpy.utils.register_class(SNA_OT_Selecionaobjetoslmerrado_0C83D)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_SPEEDWORK_0B345)
    bpy.utils.unregister_class(SNA_OT_Limpaarquivo_702D2)
    bpy.utils.unregister_class(SNA_OT_Applyall_66E0F)
    bpy.utils.unregister_class(SNA_OT_Clearparent_C9Bb3)
    bpy.utils.unregister_class(SNA_OT_Renomeiamalha_Ae2Ce)
    bpy.utils.unregister_class(SNA_OT_Autouv_B9591)
    bpy.utils.unregister_class(SNA_OT_Autolm_113C4)
    bpy.utils.unregister_class(SNA_OT_Autouvlm_Ab75F)
    bpy.utils.unregister_class(SNA_OT_Selecionaobjetosuverrado_408F4)
    bpy.utils.unregister_class(SNA_OT_Selecionaobjetoslmerrado_0C83D)
