<template>
  <v-main>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="12" md="9">
          <v-card
            class="title mb-5"
          >
            <v-card-text class="title">
              {{ currentDoc.text }}
            </v-card-text>
          </v-card>
          <seq2seq-box
            :text="currentDoc.text"
            :annotations="currentDoc.annotations"
            @delete:annotation="_deleteAnnotation"
            @update:annotation="_updateAnnotation"
            @create:annotation="_createAnnotation"
          />
        </v-col>
        <v-col cols="12" md="3">
          <list-metadata :metadata="currentDoc.meta" />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import ListMetadata from '@/components/tasks/metadata/ListMetadata'
import Seq2seqBox from '~/components/tasks/seq2seq/Seq2seqBox'

export default {

  components: {
    Seq2seqBox,
    ListMetadata
  },
  layout: 'demo',

  data() {
    return {
      currentDoc: {
        id: 8,
        text: 'If it had not been for his help, I would have failed.',
        annotations: [
          {
            id: 17,
            text: "S'il ne m'avait pas aidé, j'aurais échoué.",
            user: 1,
            document: 8
          },
          {
            id: 18,
            text: "S'il ne m'avait pas aidée, j'aurais échoué.",
            user: 1,
            document: 8
          }
        ],
        meta: { wikiPageId: 2},
        annotation_approver: null
      }
    }
  },

  methods: {
    _deleteAnnotation(annotationId) {
      this.currentDoc.annotations = this.currentDoc.annotations.filter(item => item.id !== annotationId)
    },
    _updateAnnotation(annotationId, text) {
      const index = this.currentDoc.annotations.findIndex(item => item.id === annotationId)
      this.currentDoc.annotations[index].text = text
    },
    _createAnnotation(text) {
      const payload = {
        id: Math.floor(Math.random() * Math.floor(Number.MAX_SAFE_INTEGER)),
        text
      }
      this.currentDoc.annotations.push(payload)
    }
  }
}
</script>
