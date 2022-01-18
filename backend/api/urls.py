from django.urls import include, path

from .views import (annotation, auto_labeling, comment, example, example_state,
                    export_dataset, health, label, project, tag, task)
from .views.tasks import category, relation, span, text

urlpatterns_project = [
    path(
        route='download-format',
        view=export_dataset.DownloadDatasetCatalog.as_view(),
        name='download-format'
    ),
    path(
        route='download',
        view=export_dataset.DownloadAPI.as_view(),
        name='download-dataset'
    ),
    path(
        route='category-types',
        view=label.CategoryTypeList.as_view(),
        name='category_types'
    ),
    path(
        route='category-types/<int:label_id>',
        view=label.CategoryTypeDetail.as_view(),
        name='category_type'
    ),
    path(
        route='span-types',
        view=label.SpanTypeList.as_view(),
        name='span_types'
    ),
    path(
        route='span-types/<int:label_id>',
        view=label.SpanTypeDetail.as_view(),
        name='span_type'
    ),
    path(
        route='category-type-upload',
        view=label.CategoryTypeUploadAPI.as_view(),
        name='category_type_upload'
    ),
    path(
        route='span-type-upload',
        view=label.SpanTypeUploadAPI.as_view(),
        name='span_type_upload'
    ),
    path(
        route='examples',
        view=example.ExampleList.as_view(),
        name='example_list'
    ),
    path(
        route='examples/<int:example_id>',
        view=example.ExampleDetail.as_view(),
        name='example_detail'
    ),
    path(
        route='relation_types',
        view=label.RelationTypeList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='relation_type-upload',
        view=label.RelationTypeUploadAPI.as_view(),
        name='relation_type-upload'
    ),
    path(
        route='relation_types/<int:relation_type_id>',
        view=label.RelationTypeDetail.as_view(),
        name='relation_type_detail'
    ),
    path(
        route='annotation_relations',
        view=relation.RelationList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='annotation_relation-upload',
        view=relation.RelationUploadAPI.as_view(),
        name='annotation_relation-upload'
    ),
    path(
        route='annotation_relations/<int:annotation_relation_id>',
        view=relation.RelationDetail.as_view(),
        name='annotation_relation_detail'
    ),
    path(
        route='approval/<int:example_id>',
        view=annotation.ApprovalAPI.as_view(),
        name='approve_labels'
    ),
    path(
        route='examples/<int:example_id>/categories',
        view=category.CategoryListAPI.as_view(),
        name='category_list'
    ),
    path(
        route='examples/<int:example_id>/categories/<int:annotation_id>',
        view=category.CategoryDetailAPI.as_view(),
        name='category_detail'
    ),
    path(
        route='examples/<int:example_id>/spans',
        view=span.SpanListAPI.as_view(),
        name='span_list'
    ),
    path(
        route='examples/<int:example_id>/spans/<int:annotation_id>',
        view=span.SpanDetailAPI.as_view(),
        name='span_detail'
    ),
    path(
        route='examples/<int:example_id>/texts',
        view=text.TextLabelListAPI.as_view(),
        name='text_list'
    ),
    path(
        route='examples/<int:example_id>/texts/<int:annotation_id>',
        view=text.TextLabelDetailAPI.as_view(),
        name='text_detail'
    ),
    path(
        route='tags',
        view=tag.TagList.as_view(),
        name='tag_list'
    ),
    path(
        route='tags/<int:tag_id>',
        view=tag.TagDetail.as_view(),
        name='tag_detail'
    ),
    path(
        route='examples/<int:example_id>/comments',
        view=comment.CommentListDoc.as_view(),
        name='comment_list_doc'
    ),
    path(
        route='comments',
        view=comment.CommentListProject.as_view(),
        name='comment_list_project'
    ),
    path(
        route='examples/<int:example_id>/comments/<int:comment_id>',
        view=comment.CommentDetail.as_view(),
        name='comment_detail'
    ),
    path(
      route='examples/<int:example_id>/states',
      view=example_state.ExampleStateList.as_view(),
      name='example_state_list'
    ),
    path(
        route='auto-labeling-templates',
        view=auto_labeling.AutoLabelingTemplateListAPI.as_view(),
        name='auto_labeling_templates'
    ),
    path(
        route='auto-labeling-templates/<str:option_name>',
        view=auto_labeling.AutoLabelingTemplateDetailAPI.as_view(),
        name='auto_labeling_template'
    ),
    path(
        route='auto-labeling-configs',
        view=auto_labeling.AutoLabelingConfigList.as_view(),
        name='auto_labeling_configs'
    ),
    path(
        route='auto-labeling-configs/<int:config_id>',
        view=auto_labeling.AutoLabelingConfigDetail.as_view(),
        name='auto_labeling_config'
    ),
    path(
        route='auto-labeling-config-testing',
        view=auto_labeling.AutoLabelingConfigTest.as_view(),
        name='auto_labeling_config_test'
    ),
    path(
        route='examples/<int:example_id>/auto-labeling',
        view=auto_labeling.AutoLabelingAnnotation.as_view(),
        name='auto_labeling_annotation'
    ),
    path(
        route='auto-labeling-parameter-testing',
        view=auto_labeling.AutoLabelingConfigParameterTest.as_view(),
        name='auto_labeling_parameter_testing'
    ),
    path(
        route='auto-labeling-template-testing',
        view=auto_labeling.AutoLabelingTemplateTest.as_view(),
        name='auto_labeling_template_test'
    ),
    path(
        route='auto-labeling-mapping-testing',
        view=auto_labeling.AutoLabelingMappingTest.as_view(),
        name='auto_labeling_mapping_test'
    )
]

urlpatterns = [
    path(
        route='health',
        view=health.Health.as_view(),
        name='health'
    ),
    path(
        route='projects',
        view=project.ProjectList.as_view(),
        name='project_list'
    ),
    path(
        route='tasks/status/<task_id>',
        view=task.TaskStatus.as_view(),
        name='task_status'
    ),
    path(
        route='projects/<int:project_id>',
        view=project.ProjectDetail.as_view(),
        name='project_detail'
    ),
    path('projects/<int:project_id>/', include(urlpatterns_project))
]
